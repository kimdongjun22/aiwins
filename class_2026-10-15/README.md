# 2026-10-15 수업 정리 — 도구 호출, 멀티 LLM 체인, OpenAI Agents SDK

오늘 실습한 노트북 7개와 결과, 수업에서 들은 내용을 정리했습니다.
노트북은 [notebooks/](notebooks/) 에 **실행 결과가 저장된 상태**로 들어 있습니다.

> 개인 정보 보호를 위해 노트북 출력의 개인 메일 주소는 `본인메일@gmail.com` 으로 바꾸고,
> API 키 앞자리를 찍는 셀의 출력은 지웠습니다. `.env`, 녹음 원본, 받아쓰기는 올리지 않았습니다.

## 오늘 흐름 한눈에

| 순서 | 노트북 | 배운 것 |
|---|---|---|
| 1 | [simple_tool.ipynb](notebooks/simple_tool.ipynb) | 도구 호출(Tool Calling) 기초. JSON 스키마를 손으로 쓰기 vs `@function_tool` |
| 2 | [simple_agent.ipynb](notebooks/simple_agent.ipynb) | 여러 회사 LLM을 이어 붙인 체인(CVE → CWE → 대응 방안)과 그 한계 |
| 3 | [openai_agent_intro.ipynb](notebooks/openai_agent_intro.ipynb) | OpenAI Agents SDK 기본: Agent, 도구, 핸드오프, 가드레일, 세션 |
| 4 | [openai_agent_code.ipynb](notebooks/openai_agent_code.ipynb) | 판매원 3명 영업 메일 — 에이전트를 엮는 세 가지 방법 |
| 5 | [email_agents.ipynb](notebooks/email_agents.ipynb) | 4번을 교수님 설명만 듣고 먼저 만들어 본 버전 |
| 6 | [security_briefing_by_code.ipynb](notebooks/security_briefing_by_code.ipynb) | 보안 취약점 일일 브리핑 — 순서를 **코드가** 정함 |
| 7 | [security_briefing_by_llm.ipynb](notebooks/security_briefing_by_llm.ipynb) | 같은 브리핑 — 순서를 **LLM 매니저가** 정함 |

---

## 1. 도구 호출 기초 (simple_tool)

- LLM은 함수를 실행하지 못하고 **"무엇을, 어떤 값으로 부를지"만 정한다.** 실행은 항상 우리 코드.
- 흐름: 1차 호출 → `finish_reason == "tool_calls"` → 코드가 함수 실행 → 결과를 `tool` 메시지로 붙여 2차 호출.
- `@function_tool` 은 타입 힌트와 독스트링으로 스키마를 자동 생성하고, 실행 루프까지 SDK가 처리한다.

**스스로 해 보기 풀이** (노트북 끝에 추가)

| 실험 | 결과 |
|---|---|
| `description` 을 "도구"로 대충 쓰기 | 9번 중 9번 정상 호출. 도구 **이름**이 설명 역할을 대신했다. 이름이 모호하거나 도구가 많을 때 차이가 커진다 |
| "다 모이기 전엔 호출하지 마라" 규칙 삭제 | gpt-5.4-mini 에서는 차이 없음. 규칙은 모델이 바뀌어도 흔들리지 않게 하는 보험 |
| 상담 요약 도구 추가 | 도구 이름 → 함수 사전으로 찾아 부르기. 마무리 인사에서 요약이 저장됨 |
| `while` 문으로 여러 번 처리 | 모델이 두 도구를 한 응답에서 동시에 부름. 원래 `chat()` 이었다면 엉뚱한 함수가 실행됐을 것 |

## 2. 여러 LLM 체인 (simple_agent)

- 1단계 OpenAI(CVE ID) → 2단계 Gemini(CWE ID) → 3단계 Claude(대응 방안). 앞 단계 출력을 f-string으로 다음 질문에 넣는다.
- **CVE 번호는 LLM이 가장 자주 틀리는 사실.** logprobs로 보면 `CVE-` 형식은 100% 확신, 숫자 자리는 64~67%.
- `temperature=0` 은 **일관성**을 줄 뿐 **정확성**을 주지 않는다.

**스스로 해 보기 풀이**

| 실험 | 결과 |
|---|---|
| 같은 질문 3번 | 매번 다른 CVE (2034, 2036, 2041) |
| `temperature=0` | 3번 모두 `CVE-2023-2033` — 그런데 질문 문장은 KEV에서 V8 타입 혼동 **여러 건**에 공통으로 쓰이는 설명이라 정답이 하나가 아님 |
| 형식 + NVD 존재 검사 | 정규식만으로는 부족. 형식은 맞는데 **삼성 빅스비** 취약점(CVE-2023-21465)이 나온 경우를 NVD 조회로 잡아 체인을 멈춤 |
| 모델 바꾸기 | 모델마다 CVE 번호는 다르고 CWE(유형)는 대체로 맞힘 |
| NVD 원문을 근거로 넣기 | 틀린 ID(CVE-2023-2136)를 주자 "NVD에는 CWE-190" 이라고 먼저 지적하고 구체적 버전까지 제시 → RAG가 필요한 이유 |

실행 환경 메모: `gemini-2.5-flash` 는 신규 사용자에게 404 → `gemini-3.8-flash` 사용. Gemini 무료 할당량이 실습 중 소진되어 일부는 OpenAI로 대체. Anthropic 키가 없어 Claude 단계는 건너뜀.

## 3. OpenAI Agents SDK 기본 (openai_agent_intro)

- 설치: uv 환경에는 pip이 없어서 `uv pip install --python .venv\Scripts\python.exe -U openai-agents` (0.24.0)
- 노트북에서는 `run_sync()` 가 아니라 `await Runner.run()`.
- 핸드오프 에이전트 이름이 한글이면 도구 이름이 `transfer_to______` 로 뭉개짐 → 영문 이름 사용.
- 입력 가드레일: 금칙어가 들어오면 `InputGuardrailTripwireTriggered` 로 차단.
- `SQLiteSession` 또는 `result.to_input_list()` 로 대화 이력 유지.
- 마지막 셀 버그: `async def chat` 을 `await` 없이 호출해 코루틴 객체가 출력됨 → `print(await chat(...))`.

## 4. 영업 메일 에이전트 — 엮는 방법 세 가지 (openai_agent_code)

시나리오: 윈스테크넷 **스나이퍼 APT** 영업팀. 판매원 3명(정직 / 유머 / 공격)이 메일을 쓰고, 가장 좋은 것을 골라 보낸다.

| 방식 | 누가 고르나 | 누가 보내나 | 단계 |
|---|---|---|---|
| 코드로 엮기 | LLM (메일 선택자) | 우리 코드 | Step 3~7 |
| 에이전트를 도구로 (`as_tool`) | 영업 관리자 에이전트 | 관리자가 도구로 직접 | Step 8 |
| 핸드오프 | 발송 에이전트 | 관리자가 넘겨서 발송 에이전트가 | Step 9 |

관찰
- 선택자에게 "고객이라고 상상하고 답장하고 싶은 메일을 고르라"고 하면 거의 항상 **정직한 판매원**이 뽑힌다.
- 공격적 판매원은 위기 낱말(위험·피해·지금·마비…)을 9회까지 썼다. 한 번은 지시를 거부하고 톤을 낮췄다.
- Step 8 에서 관리자가 판매원 도구를 지시(3회)보다 많은 **4회** 부른 실행이 있었다 → LLM에게 흐름을 맡기면 매번 달라질 수 있다.
- `trace("...")` 로 묶어 두면 platform.openai.com 의 **Logs → Traces** 에서 병렬 실행과 각 에이전트 입력을 볼 수 있다.

교수님 아이디어: 회사에서 나가는 모든 메일을 에이전트가 검사해, 공격적인 메일은 막는 감시 에이전트. 지금처럼 낱말 개수를 세는 것보다 LLM이 문맥으로 판단하는 편이 효과적.

### Gmail 발송 준비

`.env` 에 세 줄을 넣고 노트북의 `SEND_FOR_REAL = True` 로 바꾸면 자기 메일로 실제 발송된다.

```
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_APP_PASSWORD=구글 앱 비밀번호 16자리   # myaccount.google.com/apppasswords (2단계 인증 필요)
EMAIL_ADDRESS=본인 Gmail 주소
```

앱 비밀번호를 아직 못 받아서 노트북은 미리보기 모드로 실행했고, 고른 메일은 Claude의 Gmail 연결로 대신 보내 확인했다.

## 5. 보안 취약점 일일 브리핑 (security_briefing_by_code / by_llm)

```
[1] 자산 목록(assets.json, 가상 회사 10건)
[2] CVE 수집 — NVD 공개 API (도구)
[3] 자산 매칭 에이전트 — 키워드만 겹치는 오탐 제거, 버전 판단 (output_type=Pydantic)
[4] 위험도 평가 에이전트 — CVSS + 자산 중요도 + 인터넷 노출 → 긴급/높음/보통/낮음, 조치, 기한
[5] 담당자별 HTML 메일 발송 (팬아웃)
```

**판단은 모델에게, 계산과 조회는 코드에게.** 발송 도구는 담당자 이름만 받고, 주소·본문·중복 방지는 코드가 통제한다.

| | by_code (순서를 코드가) | by_llm (순서를 LLM 매니저가) |
|---|---|---|
| 후보 → 영향 | 40 → 32건 (제외 1건) | 40 → 23건 (제외 16건) |
| 담당자 | 5명 발송 | 5명 발송 (0건 브리핑까지 발송된 문제 있음) |
| 조건부 발송 | — | "긴급만" / "긴급·높음만" 조건을 매니저·발송 에이전트가 판단. 코드로 재검사해 5명 모두 일치 |
| 핸드오프 | — | 분석 매니저 → 메일 발송 에이전트, 미발송은 `skip_briefing_email` 로 기록 |

실행 환경 메모: `.env` 의 키 이름이 `NVD_API_KEY` 인데 노트북은 `NVD_KEY` 를 읽는다. 앱 비밀번호가 없어 발송 단계는 `DRY_RUN` 으로 실행.

---

## 남은 일

- [ ] 구글 앱 비밀번호 발급 → `.env` 의 `EMAIL_APP_PASSWORD` 채우기 → 노트북에서 직접 SMTP 발송 확인
- [ ] `.env` 에 `ANTHROPIC_API_KEY` 넣고 simple_agent 3단계(Claude) 다시 실행
- [ ] `.env` 에 `NVD_KEY` 이름으로도 키 추가 (또는 노트북을 `NVD_API_KEY` 로 수정)
- [ ] 같은 시나리오의 `langchain_agent_code.ipynb`, `langgraph_agent_code.ipynb` 실습
