# uv 명령어 레퍼런스

[uv](https://docs.astral.sh/uv/)는 Astral에서 만든 Rust 기반의 초고속 Python 패키지 및 프로젝트 관리 도구입니다.
`pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `virtualenv` 등의 기능을 하나로 통합합니다.

---

## 1. 설치 및 업데이트

| 명령어 | 설명 |
|---|---|
| `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | Windows 설치 |
| `curl -LsSf https://astral.sh/uv/install.sh \| sh` | macOS / Linux 설치 |
| `pip install uv` | pip로 설치 |
| `winget install --id=astral-sh.uv -e` | winget으로 설치 (Windows) |
| `uv self update` | uv 자체 업데이트 |
| `uv --version` | 버전 확인 |
| `uv help <command>` | 명령어 도움말 |

---

## 2. 프로젝트 관리

### 프로젝트 생성

```bash
uv init                  # 현재 디렉터리를 프로젝트로 초기화
uv init myproject        # myproject 디렉터리 생성 후 초기화
uv init --app            # 애플리케이션 프로젝트 (기본값)
uv init --lib            # 라이브러리 프로젝트 (src 레이아웃, 빌드 시스템 포함)
uv init --package        # 패키지 형태 애플리케이션 (src 레이아웃)
uv init --python 3.12    # Python 버전 지정
```

생성되는 파일: `pyproject.toml`, `.python-version`, `README.md`, `main.py`(또는 `src/`), `.gitignore`

### 의존성 추가 / 제거

```bash
uv add requests                    # 의존성 추가
uv add "requests>=2.31"            # 버전 조건 지정
uv add requests httpx              # 여러 패키지 한번에
uv add --dev pytest ruff           # 개발 의존성 추가
uv add --group lint ruff           # 특정 의존성 그룹에 추가
uv add --optional web fastapi      # optional 의존성 (extras) 추가
uv add -r requirements.txt         # requirements.txt 의 패키지 일괄 추가
uv add git+https://github.com/user/repo   # Git 저장소에서 추가
uv add --editable ./local-pkg      # 로컬 패키지를 편집 가능 모드로 추가

uv remove requests                 # 의존성 제거
uv remove --dev pytest             # 개발 의존성 제거
```

### 동기화 및 잠금

```bash
uv sync                    # uv.lock 기준으로 .venv 동기화 (없으면 생성)
uv sync --frozen           # lock 파일을 갱신하지 않고 그대로 사용
uv sync --locked           # lock 파일이 최신이 아니면 오류
uv sync --no-dev           # 개발 의존성 제외
uv sync --all-extras       # 모든 optional 의존성 포함
uv sync --extra web        # 특정 extra 포함
uv sync --group lint       # 특정 그룹 포함

uv lock                    # uv.lock 생성/갱신
uv lock --upgrade          # 모든 패키지를 최신 호환 버전으로 업그레이드
uv lock --upgrade-package requests   # 특정 패키지만 업그레이드
uv lock --check            # lock 파일이 최신인지 확인
```

### 실행

```bash
uv run main.py                 # 프로젝트 환경에서 스크립트 실행
uv run python                  # 프로젝트 환경의 Python REPL
uv run pytest                  # 프로젝트 환경의 도구 실행
uv run --with rich main.py     # 임시로 패키지를 추가하여 실행
uv run --python 3.11 main.py   # 특정 Python 버전으로 실행
uv run --no-project script.py  # 프로젝트 환경 없이 실행
```

### 조회 및 내보내기

```bash
uv tree                        # 의존성 트리 출력
uv tree --depth 1              # 깊이 제한
uv tree --outdated             # 업데이트 가능한 패키지 표시
uv export --format requirements-txt > requirements.txt   # requirements.txt로 내보내기
uv export --no-dev -o requirements.txt
```

### 버전 / 빌드 / 배포

```bash
uv version                 # 프로젝트 버전 확인
uv version 1.2.0           # 버전 설정
uv version --bump minor    # 버전 올리기 (major | minor | patch)
uv build                   # sdist 및 wheel 빌드 (dist/ 에 생성)
uv publish                 # PyPI에 배포
uv publish --token <TOKEN>
```

---

## 3. 스크립트 (단일 파일)

PEP 723 인라인 메타데이터를 이용해 스크립트별 의존성을 관리합니다.

```bash
uv run script.py                           # 스크립트 실행
uv run --with requests script.py           # 의존성을 지정하여 실행
uv init --script script.py --python 3.12   # 메타데이터가 포함된 스크립트 생성
uv add --script script.py requests         # 스크립트에 의존성 추가
uv remove --script script.py requests      # 스크립트에서 의존성 제거
uv lock --script script.py                 # 스크립트 전용 lock 파일 생성
```

인라인 메타데이터 예시:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "rich",
# ]
# ///

import requests
from rich import print

print(requests.get("https://example.com").status_code)
```

---

## 4. Python 버전 관리

```bash
uv python list                 # 설치 가능/설치된 Python 목록
uv python list --only-installed
uv python install              # 최신 Python 설치
uv python install 3.12         # 특정 버전 설치
uv python install 3.11 3.12    # 여러 버전 설치
uv python uninstall 3.11       # 제거
uv python find                 # 사용될 Python 경로 확인
uv python find 3.12
uv python pin 3.12             # .python-version 파일에 버전 고정
uv python dir                  # uv가 관리하는 Python 설치 경로
uv python upgrade              # 설치된 Python 패치 버전 업그레이드
```

---

## 5. 도구 (Tools) — pipx 대체

```bash
uvx ruff check .               # 도구를 임시 환경에서 실행 (uv tool run 의 별칭)
uvx ruff@0.6.0 check .         # 특정 버전으로 실행
uvx --from httpie http         # 패키지명과 명령어명이 다를 때
uvx --with mkdocs-material mkdocs serve   # 추가 패키지와 함께 실행

uv tool run ruff check .       # uvx 와 동일
uv tool install ruff           # 도구를 전역 설치 (PATH에 등록)
uv tool install "ruff==0.6.0"
uv tool upgrade ruff           # 도구 업그레이드
uv tool upgrade --all          # 모든 도구 업그레이드
uv tool uninstall ruff         # 도구 제거
uv tool list                   # 설치된 도구 목록
uv tool dir                    # 도구 설치 경로
uv tool update-shell           # 도구 실행 경로를 PATH에 추가
```

---

## 6. pip 호환 인터페이스

기존 `pip` / `virtualenv` / `pip-tools` 워크플로를 그대로 빠르게 사용할 수 있습니다.

### 가상환경

```bash
uv venv                        # .venv 생성
uv venv myenv                  # 이름 지정
uv venv --python 3.12          # Python 버전 지정
uv venv --seed                 # pip, setuptools 포함하여 생성
```

활성화:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate.bat
# macOS / Linux
source .venv/bin/activate

deactivate                     # 비활성화
```

### 패키지 관리

```bash
uv pip install requests            # 설치
uv pip install -r requirements.txt # requirements 파일로 설치
uv pip install -e .                # 현재 프로젝트를 편집 가능 모드로 설치
uv pip install --system requests   # 시스템 Python에 설치
uv pip uninstall requests          # 제거
uv pip list                        # 설치 목록
uv pip list --outdated             # 업데이트 가능한 목록
uv pip show requests               # 패키지 정보
uv pip freeze > requirements.txt   # 설치된 패키지 고정 출력
uv pip tree                        # 의존성 트리
uv pip check                       # 의존성 충돌 검사
```

### 컴파일 / 동기화 (pip-tools 대체)

```bash
uv pip compile requirements.in -o requirements.txt     # 고정 버전 파일 생성
uv pip compile pyproject.toml -o requirements.txt
uv pip compile requirements.in --upgrade               # 최신 버전으로 갱신
uv pip sync requirements.txt                           # 환경을 파일과 정확히 일치시킴
```

---

## 7. 캐시 관리

```bash
uv cache dir          # 캐시 경로 확인
uv cache clean        # 전체 캐시 삭제
uv cache clean requests   # 특정 패키지 캐시 삭제
uv cache prune        # 사용하지 않는 캐시 정리
```

---

## 8. 자주 쓰는 전역 옵션

| 옵션 | 설명 |
|---|---|
| `--python <ver>` / `-p` | 사용할 Python 버전/경로 지정 |
| `--directory <path>` | 지정한 디렉터리에서 명령 실행 |
| `--project <path>` | 프로젝트 디렉터리 지정 |
| `--offline` | 네트워크 접근 없이 캐시만 사용 |
| `--no-cache` | 캐시 사용 안 함 |
| `--index-url <url>` | 기본 패키지 인덱스 변경 |
| `--extra-index-url <url>` | 추가 패키지 인덱스 |
| `-q`, `--quiet` | 출력 최소화 |
| `-v`, `--verbose` | 상세 출력 |
| `--color <auto\|always\|never>` | 색상 출력 설정 |

---

## 9. 주요 환경 변수

| 변수 | 설명 |
|---|---|
| `UV_PYTHON` | 기본 Python 버전 |
| `UV_INDEX_URL` | 기본 패키지 인덱스 URL |
| `UV_EXTRA_INDEX_URL` | 추가 패키지 인덱스 URL |
| `UV_CACHE_DIR` | 캐시 디렉터리 |
| `UV_PROJECT_ENVIRONMENT` | 프로젝트 가상환경 경로 (기본 `.venv`) |
| `UV_NO_CACHE` | 캐시 비활성화 |
| `UV_OFFLINE` | 오프라인 모드 |
| `UV_LINK_MODE` | 설치 링크 방식 (`copy`, `hardlink`, `symlink`) |

---

## 10. 빠른 시작 워크플로

```bash
# 1) 새 프로젝트 만들기
uv init myproject
cd myproject

# 2) 의존성 추가
uv add requests
uv add --dev pytest ruff

# 3) 실행
uv run main.py

# 4) 테스트 / 린트
uv run pytest
uv run ruff check .

# 5) 다른 PC에서 환경 재현
git clone <repo> && cd <repo>
uv sync
```

---

## 11. 기존 도구와의 대응표

| 기존 도구 | uv 명령어 |
|---|---|
| `python -m venv .venv` | `uv venv` |
| `pip install pkg` | `uv pip install pkg` / `uv add pkg` |
| `pip freeze` | `uv pip freeze` |
| `pip-compile` | `uv pip compile` |
| `pip-sync` | `uv pip sync` |
| `pipx run tool` | `uvx tool` |
| `pipx install tool` | `uv tool install tool` |
| `pyenv install 3.12` | `uv python install 3.12` |
| `pyenv local 3.12` | `uv python pin 3.12` |
| `poetry init` | `uv init` |
| `poetry add pkg` | `uv add pkg` |
| `poetry install` | `uv sync` |
| `poetry run cmd` | `uv run cmd` |
| `poetry lock` | `uv lock` |
| `poetry build` / `publish` | `uv build` / `uv publish` |

---

> 공식 문서: https://docs.astral.sh/uv/
