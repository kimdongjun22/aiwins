"""설치한 라이브러리들이 import 되는지 확인하는 스크립트.

실행: uv run python check_imports.py
"""

import importlib

# (설치 패키지 이름, import 이름)
LIBRARIES = [
    ("python-dotenv", "dotenv"),
    ("openai", "openai"),
    ("requests", "requests"),
    ("scikit-learn", "sklearn"),
    ("gradio", "gradio"),
    ("tiktoken", "tiktoken"),
    ("anthropic", "anthropic"),
    ("google-genai", "google.genai"),
    ("langchain-openai", "langchain_openai"),
    ("langchain-chroma", "langchain_chroma"),
    ("chromadb", "chromadb"),
    ("langchain-text-splitters", "langchain_text_splitters"),
    ("openai-agents", "agents"),
    ("pywin32", "win32api"),
    ("langchain-community", "langchain_community"),
    ("GoogleScraper", "GoogleScraper"),
    ("google-serp-api", "google_serp_api"),
    ("deepagents", "deepagents"),
    ("python-pptx", "pptx"),
    ("ollama", "ollama"),
    ("torch", "torch"),
    ("pandas", "pandas"),
    ("matplotlib", "matplotlib"),
]

failed = []
for package, module in LIBRARIES:
    try:
        importlib.import_module(module)
        print(f"[OK]   {package:<26} import {module}")
    except Exception as e:
        failed.append(package)
        reason = str(e).splitlines()[0][:90]
        print(f"[FAIL] {package:<26} import {module}  -> {type(e).__name__}: {reason}")

print(f"\n성공 {len(LIBRARIES) - len(failed)} / 전체 {len(LIBRARIES)}")
if failed:
    print("실패:", ", ".join(failed))
