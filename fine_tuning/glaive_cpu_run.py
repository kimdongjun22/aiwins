"""glaive_colab.md를 GPU 없이 CPU로 끝까지(학습 → 질의) 실행한다.

문서와 다른 점은 GPU 전용 부분뿐이다.
- 4비트 양자화(bitsandbytes) 없이 fp32로 불러온다.
- fp16, paged_adamw_8bit 대신 CPU용 기본값(fp32, adamw_torch)을 쓴다.
모델, 데이터 선택(seed=42, 500/100건), LoRA 설정, 학습 횟수는 문서와 같다.

    uv run --no-project --python 3.12 --with-requirements requirements_cpu.txt python glaive_cpu_run.py
"""
import json
import os
import sys
import time

import torch
import transformers
import trl
from datasets import Dataset, load_dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
from trl import SFTConfig, SFTTrainer

print("transformers", transformers.__version__, "| trl", trl.__version__, "| torch", torch.__version__, flush=True)
print("CPU 스레드:", torch.get_num_threads(), flush=True)

BASE_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
OUTPUT_DIR = "qwen-glaive-python-cpu"
MAX_LENGTH = 256
TRAIN_SIZE = 500
VAL_SIZE = 100
# 속도만 재 볼 때: MAX_STEPS=3 환경변수로 실행
MAX_STEPS = int(os.getenv("MAX_STEPS", "-1"))

# ---- 데이터 준비 (4~10단계) ----
raw = load_dataset("glaiveai/glaive-code-assistant", split="train")
python_rows = raw.filter(lambda item: "python" in item["question"].lower())


def messages_for(item):
    message = f"Get answers for questions related to Python. Respond with answers, no explanation\n\n{item['question']}"
    return {
        "prompt": [{"role": "user", "content": message}],
        "completion": [{"role": "assistant", "content": item["answer"]}],
    }


tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)


def token_length(item):
    m = messages_for(item)
    text = tokenizer.apply_chat_template(m["prompt"] + m["completion"], tokenize=False)
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])


selected = []
for item in python_rows.shuffle(seed=42):
    if token_length(item) <= MAX_LENGTH:
        selected.append(item)
        if len(selected) == TRAIN_SIZE + VAL_SIZE:
            break
train_set = selected[:TRAIN_SIZE]
val_set = selected[TRAIN_SIZE:]
train_ds = Dataset.from_list([messages_for(item) for item in train_set])
val_ds = Dataset.from_list([messages_for(item) for item in val_set])
print("데이터:", len(train_set), len(val_set), flush=True)

# ---- 모델 적재 (11~12단계, CPU fp32) ----
model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, torch_dtype=torch.float32)
model.config.use_cache = False


def answer_for(m, item, max_new_tokens=200):
    prompt = messages_for(item)["prompt"]
    text = tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
    with torch.no_grad():
        output = m.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False,
                            pad_token_id=tokenizer.eos_token_id, use_cache=True)
    return tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)


# ---- 학습 (14~17단계) ----
peft_config = LoraConfig(
    r=8, lora_alpha=16, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
)
train_args = SFTConfig(
    output_dir=OUTPUT_DIR,
    max_length=MAX_LENGTH,
    completion_only_loss=True,
    num_train_epochs=1,
    max_steps=MAX_STEPS,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    optim="adamw_torch",
    use_cpu=True,
    logging_steps=1 if MAX_STEPS > 0 else 10,
    eval_strategy="no" if MAX_STEPS > 0 else "epoch",
    per_device_eval_batch_size=1,
    save_strategy="no",
    report_to=[],
    seed=42,
)


class StepTimer(TrainerCallback):
    """스텝마다 걸린 시간과 남은 시간 추정을 찍는다."""

    def on_train_begin(self, args, state, control, **kw):
        self.t0 = time.time()

    def on_step_end(self, args, state, control, **kw):
        el = time.time() - self.t0
        per = el / state.global_step
        left = per * (state.max_steps - state.global_step)
        print(f"[step {state.global_step}/{state.max_steps}] 스텝당 {per:.0f}초, 남은 시간 약 {left / 60:.0f}분", flush=True)

    def on_log(self, args, state, control, logs=None, **kw):
        print("[log]", json.dumps(logs, ensure_ascii=False), flush=True)


trainer = SFTTrainer(
    model=model, args=train_args, train_dataset=train_ds, eval_dataset=val_ds,
    processing_class=tokenizer, peft_config=peft_config, callbacks=[StepTimer()],
)
trainer.model.print_trainable_parameters()
t = time.time()
result = trainer.train()
print(f"학습 끝: {result} ({(time.time() - t) / 60:.1f}분)", flush=True)
if MAX_STEPS > 0:
    sys.exit(0)

trainer.save_model(OUTPUT_DIR)
print("어댑터 저장:", OUTPUT_DIR, flush=True)

# ---- 질의 (21~26단계) ----
tuned_model = trainer.model
tuned_model.eval()
tuned_model.config.use_cache = True
tokenizer.truncation_side = "left"

item = val_set[0]
print("\n" + "=" * 70)
print("[23단계] 검증 질문:", item["question"])
print("=" * 70)
print("\n[24단계] 파인튜닝한 모델의 답\n" + answer_for(tuned_model, item), flush=True)
print("\n[25단계] 데이터셋의 답\n" + item["answer"], flush=True)
with tuned_model.disable_adapter():
    print("\n[26단계] 원래 Qwen의 답\n" + answer_for(tuned_model, item), flush=True)
