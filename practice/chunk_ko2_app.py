"""chunk_basic_ko2 노트북의 Gradio 비교 화면만 따로 띄운다.
노트북이 만들어 둔 Chroma DB(chroma_chunk_ko2/)를 그대로 읽으므로 청크를 다시 임베딩하지 않는다."""
from difflib import SequenceMatcher

import chromadb
import gradio as gr
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
ai = OpenAI()

client = chromadb.PersistentClient(path="chroma_chunk_ko2")
collections = {name: client.get_collection(name) for name in ["fixed-200", "paragraphs-200"]}


def embed(texts):
    r = ai.embeddings.create(model="text-embedding-3-small", input=texts)
    V = np.asarray([d.embedding for d in r.data], dtype=np.float32)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    return V


def search_db(query, name, k=3):
    qv = embed([query])[0]
    res = collections[name].query(query_embeddings=[qv.tolist()], n_results=k)
    return [
        (1 - dist, text, meta["chunk_id"], meta["tokens"])
        for dist, text, meta in zip(res["distances"][0], res["documents"][0], res["metadatas"][0])
    ]


def diagnose(text):
    problems = []
    if "�" in text[:5]:
        problems.append("글자가 깨진 채 시작")
    if not text.rstrip().endswith((".", "!", "?", "”", "\"", "…", "-")):
        problems.append("문장 중간에서 끝남")
    return problems


def build_summary(query, fixed, paras):
    fs, ft = fixed[0][0], fixed[0][1]
    ps, pt = paras[0][0], paras[0][1]
    lines = [f"### 「{query}」 비교 결과", ""]
    winner = "문단 청킹" if ps > fs else "고정 크기 청킹"
    lines.append(f"- **점수**: 고정 크기 `{fs:.3f}` vs 문단 `{ps:.3f}` "
                 f"→ **{winner}**이 `{abs(ps - fs):.3f}` 높습니다.")
    overlap = SequenceMatcher(None, ft, pt).ratio()
    if overlap > 0.3:
        lines.append(f"- **내용**: 두 방식이 **같은 대목**을 찾았습니다 (본문 일치도 {overlap:.0%}). "
                     f"어디서 잘랐는지만 다릅니다.")
    else:
        lines.append(f"- **내용**: 두 방식이 **서로 다른 대목**을 가져왔습니다 (본문 일치도 {overlap:.0%}). "
                     f"직접 읽고 어느 쪽이 질문에 맞는지 판단해 보세요.")
    fp, pp = diagnose(ft), diagnose(pt)
    if fp:
        lines.append(f"- **잘림**: 고정 크기 1위 청크는 {', '.join(fp)}. "
                     f"한글은 글자 하나가 여러 토큰이라 토큰 경계로 자르면 글자가 깨질 수 있습니다.")
    if not pp:
        lines.append("- **잘림**: 문단 청크는 문장이 온전합니다.")
    else:
        lines.append(f"- **잘림**: 문단 1위 청크도 {', '.join(pp)} (대화체라 따옴표로 끝나는 경우가 있습니다).")
    lines.append(f"- **크기**: 고정 크기 {fixed[0][3]}토큰 / 문단 {paras[0][3]}토큰")
    return "\n".join(lines)


def format_results(title, results):
    out = [f"### {title}", ""]
    for rank, (score, text, chunk_id, tokens) in enumerate(results, 1):
        body = " ".join(text.split())
        out.append(f"**{rank}위 · 점수 {score:.3f} · 청크 {chunk_id} · {tokens}토큰**")
        out.append("")
        out.append(f"> {body[:400]}{'...' if len(body) > 400 else ''}")
        out.append("")
    return "\n".join(out)


def compare(query, k):
    if not query.strip():
        return "질문을 입력하세요.", "", ""
    k = int(k)
    fixed = search_db(query, "fixed-200", k)
    paras = search_db(query, "paragraphs-200", k)
    return (build_summary(query, fixed, paras),
            format_results("고정 크기 청킹 (fixed-200)", fixed),
            format_results("문단 청킹 (paragraphs-200)", paras))


with gr.Blocks(title="청킹 방식 비교 검색") as demo:
    gr.Markdown("# 청킹 방식 비교 검색\n"
                "「운수 좋은 날」에서 같은 질문을 **두 가지 청킹 방식**으로 검색하고 결과를 비교합니다.")
    with gr.Row():
        question = gr.Textbox(label="질문", value="아내가 앓아누워 기침하는 대목", scale=4)
        k = gr.Slider(1, 5, value=3, step=1, label="가져올 청크 수 (k)", scale=1)
    btn = gr.Button("검색", variant="primary")
    gr.Examples(
        examples=[
            ["설렁탕을 사 왔는데 왜 먹지를 못하니"],
            ["김 첨지의 아내는 어떤 상태인가?"],
            ["김 첨지가 친구 치삼과 술을 마시는 장면"],
            ["비 오는 날씨 묘사"],
            ["파이썬으로 웹 서버 만드는 법은?"],
        ],
        inputs=question,
    )
    summary_out = gr.Markdown()
    with gr.Row():
        fixed_out = gr.Markdown()
        paras_out = gr.Markdown()
    outputs = [summary_out, fixed_out, paras_out]
    btn.click(compare, inputs=[question, k], outputs=outputs)
    question.submit(compare, inputs=[question, k], outputs=outputs)

demo.launch(inbrowser=True)
