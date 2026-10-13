# 보안 공지 요약 — 모델 비교 결과

_실행: 2026-10-13 13:26:32_
_공지 10건 × 모델 4개 = 40회 호출_

## 점수표

| 모델 | 형식 | 제품 | 조치 | 지어냄 | 잘림 | 오류 | 입력토큰 | 출력토큰 | 총 초 |
|---|---|---|---|---|---|---|---|---|---|
| gpt-4.1-mini | 10/10 | 10/10 | 10/10 | **0** | 0 | 0 | 4,850 | 664 | 12.6 |
| gpt-4.1-nano | 10/10 | 10/10 | 6/10 | **0** | 0 | 0 | 4,850 | 534 | 9.6 |
| qwen2.5:3b | 10/10 | 10/10 | 7/10 | **0** | 0 | 0 | 5,088 | 933 | 174.4 |
| llama3.2 | 9/10 | 10/10 | 5/10 | **1** | 0 | 0 | 5,015 | 658 | 137.2 |

## 버전이 공지에 없는 두 건

### 4번 — GNU Bash

- **gpt-4.1-mini**: 공지에 없음
- **gpt-4.1-nano**: 공지에 없음
- **qwen2.5:3b**: 공지에 없음
- **llama3.2**: GNU Bash 4.4 이상

### 8번 — Adobe Commerce

- **gpt-4.1-mini**: 공지에 없음
- **gpt-4.1-nano**: 공지에 없음
- **qwen2.5:3b**: 공지에 없음
- **llama3.2**: 공지에 없음

## 모델별 전체 답변

### gpt-4.1-mini

**1. CVE-2021-44228 (Apache Log4j2)**

```
제품: Apache Log4j 2.x (2.14.1 이하 버전 및 2.15.0 미만 버전)
영향: 공격자가 로그 메시지 조작을 통해 원격 코드 실행(RCE)을 할 수 있음
조치: 2.16.0 이상으로 업데이트
긴급도: 긴급
```

**2. CVE-2022-22965 (Spring Framework)**

```
제품: Spring Framework 5.2.20 미만 및 5.3.18 미만  
영향: 원격에서 코드 실행이 가능하다.  
조치: 5.3.18 이상 또는 5.2.20 이상으로 업그레이드  
긴급도: 긴급
```

**3. CVE-2017-5638 (Apache Struts 2)**

```
제품: Apache Struts 2 2.3.x (2.3.32 이전), 2.5.x (2.5.10.1 이전)  
영향: 원격 공격자가 조작된 HTTP 헤더를 통해 임의 명령을 실행할 수 있음  
조치: 2.3.32 이상, 2.5.10.1 이상으로 업데이트  
긴급도: 긴급
```

**4. CVE-2014-6271 (GNU Bash)**

```
제품: GNU Bash 4.3 이하  
영향: 원격 공격자가 조작된 환경 변수를 통해 임의 코드를 실행할 수 있음  
조치: 공지에 없음  
긴급도: 긴급
```

**5. CVE-2023-49105 (ownCloud)**

```
제품: ownCloud owncloud/core 10.6.0부터 10.13.1 미만  
영향: 공격자가 인증 없이 알려진 사용자 이름으로 파일을 접근, 수정, 삭제할 수 있음  
조치: 10.13.1 이상으로 올릴 것  
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)**

```
제품: Starlette 1.0.1 미만 버전  
영향: 조작된 HTTP Host 헤더로 request.url.path와 실제 요청 경로가 달라져 보안 제한을 우회할 수 있음  
조치: 1.0.1 이상 버전으로 업그레이드  
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)**

```
제품: LiteLLM 1.84.0 이전 버전  
영향: 인증 없이 조작된 Authorization 헤더로 MCP 도구에 무단 접근 가능  
조치: 1.84.0 버전으로 업데이트  
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)**

```
제품: Adobe Commerce (영향받는 버전 공지에 없음)  
영향: 공격자가 임의의 코드를 실행할 수 있음  
조치: 공지에 없음  
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)**

```
제품: Kestra OSS 1.0.45 미만, 1.3.21 미만  
영향: 인증 없이 임의 워크플로우 생성 및 실행, 원격 코드 실행 가능  
조치: 1.0.45 이상 또는 1.3.21 이상으로 업데이트  
긴급도: 긴급
```

**10. CVE-2026-73570 (Zimbra Collaboration)**

```
제품: Zimbra Collaboration (ZCS) 10.1.20 이전 버전, zimbra-snmp 패키지 설치 및 SNMP 알림 활성화 시  
영향: 인증되지 않은 공격자가 임의의 운영 체제 명령을 실행할 수 있음  
조치: 10.1.20 이상으로 업데이트  
긴급도: 긴급
```

### gpt-4.1-nano

**1. CVE-2021-44228 (Apache Log4j2)**

```
제품: Log4j 2.14.1 이하
영향: 원격 코드 실행(RCE)이 가능
조치: 공지에 없음
긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)**

```
제품: Spring Framework 이전 버전 5.2.20, 5.3.18
영향: 원격 코드 실행(RCE)이 가능하며, JDK 9 이상, Tomcat, WAR 배포 시 취약
조치: 5.3.18, 5.2.20
긴급도: 긴급
```

**3. CVE-2017-5638 (Apache Struts 2)**

```
제품: Apache Struts 2 2.3.x before 2.3.32, 2.5.x before 2.5.10.1  
영향: 원격 공격자가 임의의 명령을 실행할 수 있음  
조치: 공지에 없음  
긴급도: 높음
```

**4. CVE-2014-6271 (GNU Bash)**

```
제품: Bash 4.3 이하
영향: 원격 공격자가 임의의 코드를 실행할 수 있음
조치: 공지에 없음
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)**

```
제품: ownCloud core 이전 버전(최초 10.6.0)
영향: 공격자가 인증 없이 파일에 접근, 수정 또는 삭제 가능
조치: 공지에 없음
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)**

```
제품: Starlette 버전 1.0.1 미만  
영향: 악의적인 사용자가 malformed Host 헤더를 통해 요청 URL을 조작할 수 있음  
조치: 1.0.1 이상으로 업그레이드  
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)**

```
제품: LiteLLM 버전 1.84.0 미만  
영향: 인증되지 않은 공격자가 무단으로 MCP 도구에 접근할 수 있음  
조치: 1.84.0  
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)**

```
제품: Adobe Commerce
영향: 공격자가 임의의 코드를 실행할 수 있음
조치: 공지에 없음
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)**

```
제품: Kestra 버전 1.0.45 이전, 1.3.21 이전  
영향: 인증 없이 임의의 워크플로우 생성 및 실행, 원격 코드 실행 가능  
조치: 1.0.45, 1.3.21  
긴급도: 긴급
```

**10. CVE-2026-73570 (Zimbra Collaboration)**

```
제품: Zimbra Collaboration 이전 버전 10.1.20 미만  
영향: 인증되지 않은 공격자가 임의의 운영체제 명령을 실행할 수 있음  
조치: 공지에 없음  
긴급도: 높음
```

### qwen2.5:3b

**1. CVE-2021-44228 (Apache Log4j2)**

```
제품: Apache Log4j
영향: 로그 메시지에 대한 JNDI 루프백이 사용되는 모든 버전의 로그4j에서 제어 가능한 코드 실행(RCE)이 가능합니다.
조치: 2.16.0
긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)**

```
제품: Spring Framework prior to versions 5.2.20 and 5.3.18
영향: Spring MVC 또는 Spring WebFlux 애플리케이션은 JDK 9 이상에서 Tomcat 컨테이너를 사용하여 WAR 배포로 실행될 경우, 데이터 바인딩을 통해 레이어 코드 실행(RCE)이 가능합니다.
조치: Spring Framework [5.3.18](https://github.com/spring-projects/spring-framework/releases/tag/v5.3.18) and [5.2.20](https://github.com/spring-projects/spring-framework/releases/tag/v5.2.20.RELEASE) 및 Spring Boot [2.6.6](https://github.com/spring-projects/spring-boot/releases/tag/v2.6.6) and [2.5.12](https://github.com/spring-projects/spring-boot/releases/tag/v2.5.12)
긴급도: 높음
```

**3. CVE-2017-5638 (Apache Struts 2)**

```
제품: Apache Struts 2 2.3.x before 2.3.32 and 2.5.x before 2.5.10.1
영향: 공격자가 적절한 Content-Type, Content-Disposition, 또는 Content-Length HTTP 헤더를 사용하여 원격 시스템에서 임의 명령을 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**4. CVE-2014-6271 (GNU Bash)**

```
제품: GNU Bash through 4.3
영향: 공격자는 특정 환경 변수를 통해 Bash에서 실행되는 서비스와 애플리케이션을 통한 권한 없이 제3자 공격자가 제공한 환경 변수를 사용하여 임의 코드 실행을 시도할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)**

```
제품: ownCloud owncloud/core
영향: 악의적인 사용자가 알 수 없는 사용자의 파일을 읽고 수정하고 삭제할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)**

```
제품: Starlette
영향: 악의적인 HTTP `Host` 요청 헤더를 사용하여 악용가능한 경로를 생성
조치: 1.0.1 버전 이상
긴급도: 중간
```

**7. CVE-2026-59822 (LiteLLM)**

```
제품: LiteLLM (영향받는 버전: 공지에 없음)
영향: 악의적인 사용자가 LiteLLM의 MCP Streamable HTTP 엔드포인트를 통해 애플리케이션에 대한 액세스를 얻을 수 있습니다.
조치: 1.84.0
긴급도: 높음
```

**8. CVE-2026-75650 (Adobe Commerce)**

```
제품: Adobe Commerce
영향: 사용자 컨텍스트에서 임의 코드 실행
조치: 공지에 없음
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)**

```
제품: Kestra (영향받는 버전: 공지에 없음)
영향: 악의적인远端 사용자가 이 문제를 이용해 API 경로의 마지막 부분이 configs인 모든 API 경로를 통과시킬 수 있어, 기본 암호화를 통한 인증을 완전히 회피할 수 있습니다. 이로 인해 악의적인 사용자는 Kestra 워커 컨테이너 내에서 루트 권한을 가진遠端 코드 실행을 수행할 수 있습니다.
조치: 1.0.45 및 1.3.21
긴급도: 높음
```

**10. CVE-2026-73570 (Zimbra Collaboration)**

```
제품: Zimbra Collaboration (ZCS) before 10.1.20
영향: 악의적인 사용자로부터 SMTP 요청을 보내면 임시 사용자로 실행되는 임의 운영 체제 명령을 실행할 수 있는 취약점
조치: 공지에 없음
긴급도: 높음
```

### llama3.2

**1. CVE-2021-44228 (Apache Log4j2)**

```
# 제품: Log4j 2.x
# 영향: 로그인한 사용자가 LDAP JNDI 파서를 사용하여 원격 코드 실행을 할 수 있습니다.
#조치: Log4j 2.16.0 이상
#긴급도: 높음
```

**2. CVE-2022-22965 (Spring Framework)**

```
제품: Spring Framework prior to versions 5.2.20 and 5.3.18
영향: Tomcat에 WAR 패키지로 배포된 Spring MVC 또는 Spring WebFlux 애플리케이션에서 원격 코드 실행 위험에 노출될 수 있습니다.
조치: Spring Framework [5.3.18]와 [5.2.20] 버전, Spring Boot [2.6.6]와 [2.5.12] 버전을 사용하십시오.
긴급도: 높음
```

**3. CVE-2017-5638 (Apache Struts 2)**

```
제품: Apache Struts 2 2.3.x before 2.3.32, 2.5.x before 2.5.10.1
영향: 공격자가 Content-Type, Content-Disposition, 또는 Content-Length HTTP header를 조작하여 원격 attacker가 원하는 명령을 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 보통
```

**4. CVE-2014-6271 (GNU Bash)**

```
제품: GNU Bash
영향: GNU Bash를 사용하는 모든 시스템에 대한 공격자가 shell 명령을 실행할 수 있습니다.
조치: GNU Bash 4.4 이상
긴급도: 높음
```

**5. CVE-2023-49105 (ownCloud)**

```
제품: ownCloud owncloud/core
영향: 공격자가 특정 사용자 이름을 biết고, 사용자가 signing-key를 구성하지 않은 경우 파일을 수정하거나 삭제할 수 있습니다.
조치: ownCloud owncloud/core 10.13.1 이상
긴급도: 높음
```

**6. CVE-2026-48710 (Starlette)**

```
제품: Starlette 1.0.1
영향: maliciously crafted HTTP `Host` request header를 사용하여 request.url.path와 canonical ASGI request path (scope["path"])의 차이를 만들 수 있습니다.
조치: Starlette 1.0.1 이상
긴급도: 보통
```

**7. CVE-2026-59822 (LiteLLM)**

```
제품: LiteLLM 1.84.0
영향: LiteLLM proxy server의 MCP Streamable HTTP 엔드포인트를 사용하여 OAuth2 passthrough fallback path를 bypass할 수 있다.
조치: LiteLLM 1.84.0
긴급도: 보통
```

**8. CVE-2026-75650 (Adobe Commerce)**

```
제품: Adobe Commerce
영향: 공격자가 현재 사용자 contexto에서 arbitrar리 코드를 실행할 수 있습니다.
조치: 공지에 없음
긴급도: 높음
```

**9. CVE-2026-49869 (Kestra)**

```
제품: Kestra OSS
영향: unauthenticated Remote Code Execution as root inside the Kestra worker container
조치: 공지에 없음
긴급도: 높음
```

**10. CVE-2026-73570 (Zimbra Collaboration)**

```
제품: Zimbra Collaboration (ZCS) before 10.1.20
영향: SNMP notifications를 활성화한 경우, 특수한 SMTP 요청을 보내면 arbitrary operating system commands를 실행할 수 있습니다.
조치: zimbra-snmp 패키지를 제거하십시오.
긴급도: 높음
```
