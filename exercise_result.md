# 보안 공지 요약 — 모델 비교 결과

- 실행 시각: 2026-10-13 10:29:20
- 공지 10건 × 모델 4개 = 40회 호출, temperature=0

## 점수표

| 모델 | 형식 | 제품 | 조치 | 지어냄 | 잘림 | 오류 | 입력토큰 | 출력토큰 | 총토큰 | 총 초 | 건당 초 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gpt-4.1-mini | 10/10 | 10/10 | 10/10 | **0** | 0 | 0 | 5,240 | 659 | 5,899 | 14.5 | 1.4 |
| gpt-4.1-nano | 10/10 | 10/10 | 6/10 | **0** | 0 | 0 | 5,240 | 567 | 5,807 | 9.6 | 1.0 |
| qwen2.5:3b | 10/10 | 10/10 | 8/10 | **0** | 0 | 0 | 5,498 | 911 | 6,409 | 158.6 | 15.9 |
| llama3.2 | 10/10 | 10/10 | 6/10 | **2** | 0 | 0 | 5,405 | 756 | 6,161 | 164.8 | 16.5 |

## 버전이 공지에 없는 두 건 (4번·8번)

### 4번 — GNU Bash

- **gpt-4.1-mini**: 공지에 없음
- **gpt-4.1-nano**: 공지에 없음
- **qwen2.5:3b**: 공지에 없음
- **llama3.2**: GNU Bash 4.4 이상 ← 지어냄

### 8번 — Adobe Commerce

- **gpt-4.1-mini**: 공지에 없음
- **gpt-4.1-nano**: 공지에 없음
- **qwen2.5:3b**: 공지에 없음
- **llama3.2**: Adobe Commerce 2.3.3f1 및 이후 버전을 올려야 합니다. ← 지어냄

## '공지에 없음' 지시를 뺐을 때 (gpt-4.1-mini, 3회씩)

| 번호 | 지시 | 회차 | 지어냄 | 조치 |
|---|---|---|---|---|
| 4 | 지시 있음 | 1 | 아니오 | 공지에 없음 |
| 4 | 지시 있음 | 2 | 아니오 | 공지에 없음 |
| 4 | 지시 있음 | 3 | 아니오 | 공지에 없음 |
| 4 | 지시 없음 | 1 | 예 | 4.3 이후 버전으로 업데이트 |
| 4 | 지시 없음 | 2 | 예 | 4.3 이후 버전으로 업데이트 |
| 4 | 지시 없음 | 3 | 예 | 최신 버전으로 업데이트 필요 (4.3 이후 패치 적용 버전) |
| 8 | 지시 있음 | 1 | 아니오 | 공지에 없음 |
| 8 | 지시 있음 | 2 | 아니오 | 공지에 없음 |
| 8 | 지시 있음 | 3 | 아니오 | 공지에 없음 |
| 8 | 지시 없음 | 1 | 아니오 | 최신 버전으로 업데이트 권장 |
| 8 | 지시 없음 | 2 | 아니오 | 최신 보안 패치 적용 권고 |
| 8 | 지시 없음 | 3 | 아니오 | 최신 버전으로 업데이트 권장 |

## 모델별 전체 답변

### gpt-4.1-mini

**1. CVE-2021-44228 (Apache Log4j2)** — finish_reason=stop, 839+56 토큰, 2.2초

```
제품: Apache Log4j 2.x, 2.15.0 이전 버전
영향: 공격자가 원격에서 임의 코드를 실행할 수 있음
조치: 2.16.0 이상으로 업데이트
긴급도: 긴급
```

**2. CVE-2022-22965 (Spring Framework)** — finish_reason=stop, 683+62 토큰, 1.3초

```
제품: Spring Framework 5.2.20 미만 및 5.3.18 미만  
영향: 원격에서 코드 실행이 가능하다.  
조치: 5.3.18 이상 또는 5.2.20 이상으로 업데이트  
긴급도: 긴급
```

**3. CVE-2017-5638 (Apache Struts 2)** — finish_reason=stop, 623+90 토큰, 1.2초

```
제품: Apache Struts 2 2.3.x (2.3.32 이전), 2.5.x (2.5.10.1 이전)  
영향: 원격 공격자가 조작된 HTTP 헤더를 통해 임의 명령을 실행할 수 있음  
조치: 2.3.32 이상, 2.5.10.1 이상으로 업데이트  
긴급도: 긴급
```

**4. CVE-2014-6271 (GNU Bash)** — finish_reason=stop, 420+49 토큰, 1.3초

```
제품: GNU Bash 4.3 이하 버전  
영향: 원격 공격자가 조작된 환경 변수를 통해 임의 코드를 실행할 수 있음  
조치: 공지에 없음  
긴급도: 긴급
```

**5. CVE-2023-49105 (ownCloud)** — finish_reason=stop, 324+72 토큰, 1.4초

```
제품: ownCloud owncloud/core 10.6.0부터 10.13.1 미만 버전  
영향: 공격자가 피해자의 사용자 이름만 알면 인증 없이 파일을 접근, 수정, 삭제할 수 있음  
조치: 10.13.1 이상으로 올려야 함  
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)** — finish_reason=stop, 722+72 토큰, 1.9초

```
제품: Starlette 1.0.1 미만 버전  
영향: 조작된 HTTP Host 헤더로 request.url.path와 실제 요청 경로가 달라져 보안 제한을 우회할 수 있음  
조치: 1.0.1 이상 버전으로 업그레이드  
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)** — finish_reason=stop, 610+69 토큰, 1.2초

```
제품: LiteLLM proxy 서버, 1.84.0 이전 버전  
영향: 인증되지 않은 공격자가 조작된 Authorization 헤더로 키 검증을 우회해 MCP 도구에 무단 접근 가능  
조치: 1.84.0 버전으로 업데이트  
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)** — finish_reason=stop, 300+37 토큰, 1.1초

```
제품: Adobe Commerce 모든 버전  
영향: 공격자가 임의의 코드를 실행할 수 있음  
조치: 공지에 없음  
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)** — finish_reason=stop, 400+75 토큰, 1.6초

```
제품: Kestra OSS 1.0.45 미만 및 1.3.21 미만  
영향: 인증 없이 임의의 워크플로우를 생성 및 실행하여 원격 코드 실행이 가능함  
조치: 1.0.45 및 1.3.21 이상으로 업데이트  
긴급도: 긴급
```

**10. CVE-2026-73570 (Zimbra Collaboration)** — finish_reason=stop, 319+77 토큰, 1.3초

```
제품: Zimbra Collaboration (ZCS) 10.1.20 이전 버전, zimbra-snmp 패키지 설치 및 SNMP 알림 활성화 시  
영향: 인증되지 않은 공격자가 임의의 운영 체제 명령을 실행할 수 있음  
조치: 10.1.20 이상으로 업데이트  
긴급도: 높음
```

### gpt-4.1-nano

**1. CVE-2021-44228 (Apache Log4j2)** — finish_reason=stop, 839+41 토큰, 1.4초

```
제품: Log4j 2.14.1 이하
영향: 원격 코드 실행(RCE) 공격이 가능
조치: 공지에 없음
긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)** — finish_reason=stop, 683+89 토큰, 1.0초

```
제품: Spring Framework 이전 버전 5.2.20, 5.3.18
영향: JDK 9 이상에서 Tomcat을 사용하는 WAR 배포된 Spring MVC 또는 Spring WebFlux 애플리케이션이 원격 코드 실행에 취약할 수 있음
조치: 5.3.18 또는 5.2.20으로 업그레이드
긴급도: 높음
```

**3. CVE-2017-5638 (Apache Struts 2)** — finish_reason=stop, 623+65 토큰, 1.0초

```
제품: Apache Struts 2 2.3.x 이전 버전, 2.5.x 이전 버전
영향: 원격 공격자가 조작된 HTTP 헤더를 통해 임의의 명령을 실행할 수 있음
조치: 공지에 없음
긴급도: 높음
```

**4. CVE-2014-6271 (GNU Bash)** — finish_reason=stop, 420+43 토큰, 0.8초

```
제품: GNU Bash 4.3 이하
영향: 원격 공격자가 환경 변수를 이용해 임의의 코드 실행 가능
조치: 공지에 없음
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)** — finish_reason=stop, 324+45 토큰, 1.0초

```
제품: ownCloud core 버전 10.6.0 이전
영향: 공격자가 인증 없이 파일에 접근, 수정 또는 삭제 가능
조치: 공지에 없음
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)** — finish_reason=stop, 722+64 토큰, 0.9초

```
제품: Starlette 버전 1.0.0 이하  
영향: 공격자가 malformed Host 헤더를 통해 request.url.path를 조작하여 보안 제한을 우회할 수 있음  
조치: 1.0.1 이상으로 업그레이드  
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)** — finish_reason=stop, 610+54 토큰, 0.9초

```
제품: LiteLLM 버전 1.84.0 미만
영향: 공격자가 인증 없이 MCP 도구에 접근하여 무단 작업 수행 가능
조치: 1.84.0 이상으로 업데이트
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)** — finish_reason=stop, 300+34 토큰, 0.8초

```
제품: Adobe Commerce
영향: 공격자가 임의의 코드를 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)** — finish_reason=stop, 400+76 토큰, 0.9초

```
제품: Kestra 버전 1.0.45 이전, 1.3.21 이전  
영향: 인증 없이 임의의 워크플로우 생성 및 실행, 루트 권한으로 원격 코드 실행 가능  
조치: 1.0.45 또는 1.3.21 이상으로 업데이트  
긴급도: 높음
```

**10. CVE-2026-73570 (Zimbra Collaboration)** — finish_reason=stop, 319+56 토큰, 0.9초

```
제품: Zimbra Collaboration (ZCS) 버전 10.1.20 미만  
영향: 인증되지 않은 공격자가 임의의 운영체제 명령을 실행할 수 있음  
조치: 공지에 없음  
긴급도: 높음
```

### qwen2.5:3b

**1. CVE-2021-44228 (Apache Log4j2)** — finish_reason=stop, 885+92 토큰, 36.4초

```
제품: Apache Log4j
영향: 로그 로딩 시 로그 메시지나 파라미터에 대한 악용으로 인해 애플리케이션에서 제어 가능한 리소스에 대한 제어 권한을 가진 악용자에게서 제어 가능한 코드 실행이 가능합니다.
조치: 2.16.0
긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)** — finish_reason=stop, 709+138 토큰, 23.3초

```
제품: Spring Framework 및 Spring Boot
영향: Spring MVC 또는 Spring WebFlux 애플리케이션에서 JDK 9 이상을 사용하여 Tomcat을 Servlet 컨테이너로 사용할 경우, WAR 배포로 애플리케이션을 배포하면 데이터 바인딩을 통해 레이어에서 레이어까지의 코드 실행이 가능할 수 있습니다.
조치: Spring Framework [5.3.18], [5.2.20], Spring Boot [2.6.6], [2.5.12]
긴급도: 높음
```

**3. CVE-2017-5638 (Apache Struts 2)** — finish_reason=stop, 650+59 토큰, 13.6초

```
제품: Apache Struts 2 2.3.x, 2.5.x
영향: 공격자가 malicious Content-Type 값을 사용하여 원격 코드 실행을 수행할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**4. CVE-2014-6271 (GNU Bash)** — finish_reason=stop, 442+86 토큰, 11.3초

```
제품: GNU Bash through 4.3
영향: 공격자는 특정 환경 변수를 통해 Bash에서 실행되는 서비스와 애플리케이션을 통한 권한 없이 제3자 공격자가 제공한 환경 변수를 사용하여 shell 명령을 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)** — finish_reason=stop, 346+68 토큰, 7.8초

```
제품: ownCloud owncloud/core
영향: 공유된 액세스 URL을 통해 파일을 읽기, 쓰기, 삭제할 수 있는 악용가능한 공격이 발생
조치: 10.13.1
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)** — finish_reason=stop, 746+87 토큰, 18.1초

```
제품: Starlette
영향: HTTP `Host` 요청 헤더가 사용되지 않은 상태에서 잘못된 헤더로 인해 `request.url`가 잘못 재구성될 수 있습니다. 이로 인해 `request.url.path`가 실제 요청한 경로와 다를 수 있습니다.
조치: 1.0.1 버전 이상
긴급도: 중등급
```

**7. CVE-2026-59822 (LiteLLM)** — finish_reason=stop, 635+108 토큰, 17.3초

```
제품: LiteLLM (영향받는 버전: 1.84.0 이전)
영향: 악용 가능한 오퍼스 헥 헤더를 사용하여 악용자는 키 검증을 통과하지 못한 악용자 액세스를 통해 MCP 툴링에 대한 요청을 처리할 수 있게 됩니다.
조치: 1.84.0 버전 이상
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)** — finish_reason=stop, 320+48 토큰, 5.6초

```
제품: Adobe Commerce
영향: 사용자 컨텍스트에서 현재 사용자 권한으로 임의 코드 실행이 가능합니다.
조치: 공지에 없음
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)** — finish_reason=stop, 424+142 토큰, 16.2초

```
제품: Kestra (open-source, event-driven orchestration platform)
영향: 악용자에게 API 경로의 마지막 부분이 configs인 API에 대한 접근 권한이 없어도 임의 작업을 생성하고 실행할 수 있게 됩니다. 또한 Kestra는 기본 설정에서 스크립트 실행 플러그인을 활성화하고 있으므로, Kestra 워커 컨테이너 내에서 루트 권한을 가진遠程 코드 실행이 가능합니다.
조치: 1.0.45 및 1.3.21
긴급도: 높음
```

**10. CVE-2026-73570 (Zimbra Collaboration)** — finish_reason=stop, 341+83 토큰, 9.0초

```
제품: Zimbra Collaboration (ZCS) before 10.1.20
영향: 악의적인 사용자로부터 SMTP 요청을 보내면 임시 사용자로 실행되는 임의 운영 체제 명령을 실행할 수 있는 보안 침해가 발생
조치: 공지에 없음
긴급도: 높음
```

### llama3.2

**1. CVE-2021-44228 (Apache Log4j2)** — finish_reason=stop, 854+100 토큰, 38.4초

```
제품: Log4j
영향: 로그인된 사용자에게 로그 메시지에 대한 제어를 제공하는 JNDI 파서를 통해 원격 코드 실행 위험이 발생할 수 있습니다.
조치: Log4j 2.16.0 버전을 사용하거나, 2.15.0 버전에서 JNDI 파서를 비활성화하는 것을 고려해 보세요.
긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)** — finish_reason=stop, 698+110 토큰, 21.3초

```
제품: Spring Framework prior to versions 5.2.20 and 5.3.18
영향: JDK 9+에서 Tomcat을 사용하는 Spring MVC 또는 Spring WebFlux 애플리케이션에 대해 원격 코드 실행 위험
조치: Spring Framework [5.3.18] 및 [5.2.20], Spring Boot [2.6.6] 및 [2.5.12] 업그레이드를 적용하십시오
긴급도: 보통
```

**3. CVE-2017-5638 (Apache Struts 2)** — finish_reason=stop, 641+84 토큰, 18.0초

```
제품: Apache Struts 2 2.3.x before 2.3.32, 2.5.x before 2.5.10.1
영향: 원격 공격자가 Content-Type, Content-Disposition, 또는 Content-Length HTTP 헤더를 조작하여 원격에서 명령을 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 보통
```

**4. CVE-2014-6271 (GNU Bash)** — finish_reason=stop, 435+47 토큰, 8.9초

```
제품: GNU Bash
영향: 원격 공격자가 environment variable의 value를 조작하여 shell command를 실행할 수 있습니다.
조치: GNU Bash 4.4 이상
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)** — finish_reason=stop, 340+67 토큰, 8.8초

```
제품: ownCloud owncloud/core
영향: 공격자가 특정 사용자 이름을 biết고, 사용자가 signing-key를 구성하지 않은 경우 파일을 수정하거나 삭제할 수 있습니다.
조치: ownCloud owncloud/core 버전 10.13.1 이상
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)** — finish_reason=stop, 739+73 토큰, 21.2초

```
제품: Starlette
영향: maliciously crafted HTTP `Host` request header를 사용하여 request.url.path와 실제 요청된 경로가 다르게 reconstruct되기 때문에 보안 제한이 bypass될 수 있습니다.
조치: Starlette 버전 1.0.1 이상을 사용하십시오.
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)** — finish_reason=stop, 629+93 토큰, 22.2초

```
제품: LiteLLM
영향: LiteLLM proxy server의 MCP Streamable HTTP 엔드포인트를 사용하여 오라치 2.0 패스-through fallback 패스에 취약하여 공격자가 무authenticated으로 Authorization 헤더를 사용하여 LiteLLM 키 유효성 확인을ypass할 수 있습니다.
조치: LiteLLM 1.84.0 버전
긴급도: 보통
```

**8. CVE-2026-75650 (Adobe Commerce)** — finish_reason=stop, 317+56 토큰, 7.8초

```
제품: Adobe Commerce
영향: 공격자가 현재 사용자 contexto에서 임의의 코드를 실행할 수 있습니다.
조치: Adobe Commerce 2.3.3f1 및 이후 버전을 올려야 합니다.
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)** — finish_reason=stop, 417+50 토큰, 9.2초

```
제품: Kestra OSS
영향: unauthenticated Remote Code Execution as root inside the Kestra worker container
조치: 1.0.45 및 1.3.21
긴급도: 높음
```

**10. CVE-2026-73570 (Zimbra Collaboration)** — finish_reason=stop, 335+76 토큰, 9.0초

```
제품: Zimbra Collaboration (ZCS) before 10.1.20
영향: SNMP notifications를 활성화한 경우, 비Authenticated 공격자가 특정 SMTP 요청을 보낼 수 있습니다.
조치: zimbra-snmp 패키지를 제거하고 SNMP notifications를 비활성화해야 합니다.
긴급도: 높음
```
