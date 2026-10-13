import os

import ollama
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPT = "한 문장으로 자기소개 해줘."


def run_openai() -> None:
    client = OpenAI()  # OPENAI_API_KEY 를 .env 에서 자동으로 읽음
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": PROMPT}],
    )
    print("[OpenAI gpt-4o-mini]", response.choices[0].message.content)


def run_ollama(model: str) -> None:
    # .env 의 OLLAMA_URL 은 OpenAI 호환 주소(/v1)라서, ollama 라이브러리에는 /v1 을 떼고 넘깁니다.
    host = os.getenv("OLLAMA_URL", "http://localhost:11434").removesuffix("/v1")
    client = ollama.Client(host=host)
    response = client.chat(model=model, messages=[{"role": "user", "content": PROMPT}])
    print(f"[Ollama {model}]", response.message.content)


if __name__ == "__main__":
    run_openai()
    run_ollama("llama3.2:3b")
    run_ollama("qwen2.5:3b")
