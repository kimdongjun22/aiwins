"""chunk_basic_ko3 노트북의 RAG(검색 + LLM 답변)를 Gradio 화면으로 띄운다.
노트북이 만들어 둔 Chroma DB(chroma_chunk_ko3/)를 그대로 읽으므로 청크를 다시 임베딩하지 않는다."""
import chromadb
import gradio as gr
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
ai = OpenAI()

EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4.1-mini"

client = chromadb.PersistentClient(path="chroma_chunk_ko3")
collections = {name: client.get_collection(name) for name in ["fixed-200", "paragraphs-200"]}


def embed(texts):
    r = ai.embeddings.create(model=EMBED_MODEL, input=texts)
    V = np.asarray([d.embedding for d in r.data], dtype=np.float32)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    return V


def search_db(qv, name, k=3):
    """(점수, 본문, 출처, 토큰수) 리스트를 돌려준다. 질문 벡터는 미리 받아 두 컬렉션에 재사용한다."""
    res = collections[name].query(query_embeddings=[qv.tolist()], n_results=k)
    return [
        {"score": 1 - dist, "text": text, "source": meta["source"], "tokens": meta["tokens"]}
        for dist, text, meta in zip(res["distances"][0], res["documents"][0], res["metadatas"][0])
    ]


SYSTEM_PROMPT = """당신은 정보보안 교육 자료를 안내하는 도우미입니다.

아래 [자료]에 있는 내용만 근거로 답변하세요.
- [자료]에 없는 내용은 추측하지 말고 "제공된 자료에서 찾을 수 없습니다"라고 답하세요.
- 문장 끝에 근거가 된 자료 번호를 [1], [2] 형식으로 표시하세요.
- 한국어로, 3~5문장으로 간결하게 답하세요.

[자료]
{context}
"""


def build_context(hits):
    return "\n\n".join(f"[{i}] (출처: {h['source']})\n{h['text']}" for i, h in enumerate(hits, 1))


def answer(query, qv, name, k, threshold):
    """검색 -> (하한선 검사) -> LLM 답변. 1위 점수가 하한선보다 낮으면 LLM을 부르지 않는다."""
    hits = search_db(qv, name, k)
    if hits[0]["score"] < threshold:
        return f"관련 자료가 없습니다. (1위 점수 {hits[0]['score']:.3f} < 하한선 {threshold:.2f}, LLM 호출 안 함)", hits
    response = ai.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.format(context=build_context(hits))},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content, hits


def format_panel(title, text, hits):
    out = [f"### {title}", "", f"**답변**", "", text, "", "---", "", "**근거 청크**", ""]
    for i, h in enumerate(hits, 1):
        body = " ".join(h["text"].split())
        out.append(f"**[{i}] {h['source']} · 점수 {h['score']:.3f} · {h['tokens']}토큰**")
        out.append("")
        out.append(f"> {body[:300]}{'...' if len(body) > 300 else ''}")
        out.append("")
    return "\n".join(out)


def run(query, k, threshold):
    if not query.strip():
        return "질문을 입력하세요.", ""
    qv = embed([query])[0]
    k = int(k)
    panels = []
    for name, label in [("fixed-200", "고정 크기 청킹 (fixed-200)"),
                        ("paragraphs-200", "문단 청킹 (paragraphs-200)")]:
        text, hits = answer(query, qv, name, k, threshold)
        panels.append(format_panel(label, text, hits))
    return tuple(panels)


with gr.Blocks(title="보안 문서 RAG") as demo:
    gr.Markdown("# 보안 문서 RAG\n"
                "위키백과 보안 문서 4개(정보 보안 · 피싱 · SQL 삽입 · 사이트 간 스크립팅)를 검색해 "
                "**근거와 함께 답변**합니다. 같은 질문을 두 청킹 방식으로 나란히 비교합니다.")

    with gr.Row():
        question = gr.Textbox(label="질문", value="피싱 공격은 어떤 방식으로 이루어지나요?", scale=4)
        k = gr.Slider(1, 10, value=3, step=1, label="가져올 청크 수 (k)", scale=1)
        threshold = gr.Slider(0.0, 0.6, value=0.0, step=0.05, label="점수 하한선 (0 = 끄기)", scale=1)

    btn = gr.Button("질문하기", variant="primary")

    gr.Examples(
        examples=[
            ["정보 보안의 세 가지 핵심 요소는 무엇인가요?"],
            ["피싱 메일을 어떻게 구별하나요?"],
            ["SQL 삽입 공격을 막으려면 어떻게 해야 하나요?"],
            ["준비된 선언으로 SQL 삽입을 막는 방법"],
            ["랜섬웨어에 감염되면 몇 분 안에 신고해야 하나요?"],
        ],
        inputs=question,
    )

    with gr.Row():
        fixed_out = gr.Markdown()
        paras_out = gr.Markdown()

    outputs = [fixed_out, paras_out]
    btn.click(run, inputs=[question, k, threshold], outputs=outputs)
    question.submit(run, inputs=[question, k, threshold], outputs=outputs)

demo.launch(server_port=7861, inbrowser=True)
