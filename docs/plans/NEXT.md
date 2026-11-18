# NEXT — 다음 작업 전망

## 기준

- 마지막 갱신: 2026-11-17 · 직전 완료 작업: `docs/plans/2026-11-17/org-publish/` · 기준 커밋: main 첫 커밋(README 추가) · 병합 상태: 완료(조직 origin에 push됨)

## 다음 작업 후보 (우선순위순)

### N1. 문서 작성 규칙 정리 (첫 규칙) — 우선순위: 높음 · 사용자가 지정한 첫 주제

- **왜 다음인가**: 탐색을 마쳤고 방향이 정해졌다 — "원본은 그대로 두고 여기에 하나로 정리"(사용자).
- **발생 가능한 문제**: 탐색에서 형식 규칙 충돌 4건 관측(그림 형식 ASCII·Mermaid·코드 생성 / 비ASCII 기호 금지 범위 / 한 문장 한 줄 대 문단 3~7문장 / 표·강조 허용 범위) → 범위를 적지 않고 합치면 같은 충돌이 이 저장소 안에서 재현된다.
- **권장 대처**: 공통 원칙 1 + 도식 1 + 유형별 문서로 나누고 충돌은 유형별 범위로 명시(메인 제안, 사용자 미확정).
- **확정된 결정(2026-11-17 사용자)**:
  - 유형 범위 = 작업 기록 · 학습 노트 · 해설·설계 문서 · 협업 문서 전부.
  - 그림 = 기본 ASCII, 설계 문서만 Mermaid.
  - 형식 충돌 = 기본값 하나 + 유형별 예외. 줄바꿈 기본 = 문단 3~7문장(학습 노트만 한 문장 한 줄), 표 = 값 비교일 때만(작업 기록·대장은 표 유지), 강조 = 문단당 하나.
  - 특수 기호 = "해당 문자들이 깨질 일이 없다면 사용해도 될 것 같고" → 기본 허용, 깨지는 매체만 제한(메인 해석).
  - 개인 문서 = 일반화한 규칙만. 이력서 규칙에서 가져올 것은 "자연스러운 한글 번역에 대한 규칙과 잘 읽히게 하려면 어떻게 하는지에 대한 내용 정도". 이력서·지원동기 자체는 "그 내용들을 같이 대화로 풀어나가 보자"(별도 대화).
  - 구조 = `ROUTING.md` + `writing/`(principles · diagrams · work-records · study-notes · walkthroughs · design-docs · collaboration). 규칙 문서 형식 = 언제 적용하나 / 규칙 / 예외 / 출처.
  - 진행 = auto + 묶음별 확인. 먼저 ROUTING · principles · diagrams · work-records 4개를 쓰고 확인받은 뒤 나머지.
  - 순서 = 하네스 실험(N2)을 먼저 띄우고, 이 작업은 실험이 도는 동안 다듬는다(사용자).
- **착수 전 확인할 것**: 명세서 작성(위 결정으로 6칸 채움). 옮길 원문은 메인이 직접 읽는다(탐색 워커가 못 읽은 것: evidence 1~10, jun-bank 양식 대부분, 실제 노트 샘플).
- **출처 지도**: `study-note/reference/study-note-guide.md`(§3 도식) · `study-note/project/jun-bank/workflow/writing-methodology.md`(WM-1~10) · `study-note/reference/writing/` · `study-note/cs/README.md` · `study-note/issue/authoring-guide.md` · 하네스 `templates/`·`playbooks/` · `*-ko-docs/STYLE-GUIDE.md` 4개 · `myway/docs/문제집-작성-계약.md` · `resume/작성_규칙.md`·`내정보/문장_규칙.md` · `handover/handover-template.md` 부록 C.

### N2. need-haness-lab 실험 재개 (Claude 전용) — 우선순위: 높음 · 사용자 지시

- **왜 다음인가**: 사용자 결정 — Codex는 쓰지 않고 Claude로 진행, 진행자는 Opus 에이전트, 비용은 다른 실험과 같은 방식.
- **발생 가능한 문제**: Claude 쪽 실행기가 옛 기준(v1, 토큰 상한 200만, 외부 리뷰어 없음)이고 스크립트 5종이 없다(조사 워커 보고) → 그대로는 30회를 돌릴 수 없다. 하네스 조건의 리뷰가 codex 병렬로 설계돼 있어 "Codex 미사용"과 충돌한다.
- **확정된 결정(2026-11-17 사용자)**: 진행자 = Opus 에이전트 · Codex 미사용, Claude로 진행 · 하네스 조건의 두 번째 리뷰어는 Claude 모델로 대체 · 모델은 현재 최신 버전(구현자·워커 Opus 5.5, 하네스 조건 PM Fable 5.2) · 비용은 다른 실험과 같은 방식, 처리 주체는 사용자.
- **착수 전 확인할 것**: 명세는 `need-haness-lab/docs/plans/`에 새로 연다. 기존 Codex 산출물 처리, Claude 쪽 실행기 보강 범위, 인증 토큰 재발급(사용자 소관).

### N3. 폴더 이동 뒷정리 — 우선순위: 낮음

- 이동과 세션 이전은 확인 완료(2026-11-17). 남은 것: 쓰고 난 `agent-discipline/finish-move.sh` 삭제(사용자 판단), need-harness-lab `payment-settlement/codex/scripts/prepare.py:36`의 하네스 옛 경로(지금 실행하면 실패 — 실험 준비 N2에서 처리).
- 세션은 조직 폴더(`/home/jun/project/agent-discipline`, git 저장소 아님)에서 연다. 게이트 상태파일은 `agent-discipline/.claude/lazymode/`에 생긴다.

### N4. 문서 속 개인 계정 주소·옛 저장소 이름 수정 — 우선순위: 낮음

- README 2개(rules 제목·하네스 링크, harness 복제 안내)는 고쳤다. 남은 것: 하네스 정책 파일의 "소스 repo: claude-code-harness" 표기(배포 필요), 다른 프로젝트 `settings.local.json`의 하네스 옛 경로 권한(resume, dev-questions).
- 개인 주소가 적힌 파일 약 10개(5개 저장소). 개인 계정 사본이 남아 있어 옛 링크는 그 사본을 계속 가리킨다.
- 조직 소개 글의 need-haness-lab 문구("본 실험은 아직 진행 전")는 실험 진행에 맞춰 갱신.

### N5. 하네스에 응답 언어 강제 추가 — 우선순위: 중간 · 사용자 요청(2026-11-17), 대상 저장소 = harness

- **왜 다음인가**: 사용자 — "하네스에 응답 언어를 별도로 기억해놓고 이걸 항상 응답이 지킬 수 있도록 강제". 현재 설정·훅·정책에 언어 항목이 없다(확인: `~/.claude/settings.json`, harness `hooks/*.sh`·`src/core.md`).
- **발생 가능한 문제**: 이번 세션에서 blind 테스트 워커가 보고를 영어로 냈다(관측) → 서브에이전트는 메인과 다른 경로로 지시를 받는다.
- **공식 문서 확인 결과(claude-code-guide, 2026-11-17)**: settings.json `language` 키가 있다(값은 언어 이름 문자열, 지시일 뿐 강제 아님, 서브에이전트 적용 여부는 문서에 없음). Stop 훅은 `last_assistant_message`를 받고 `{"decision":"block","reason":…}`로 되돌릴 수 있으며 `stop_hook_active`로 반복을 막는다(연속 8회 상한도 있음). SubagentStop도 같은 방식이나, 서브에이전트가 보고 도구로 낸 보고서는 `last_assistant_message`에 들어오지 않는다. UserPromptSubmit 주입은 프롬프트 제출 때 한 번뿐이다.
- **확정된 결정(2026-11-17 사용자)**: 적용 대상 = 메인 응답만 · 언어 값 = 전역 설정 한 곳 · 위반 시 = 한 번 되돌려 다시 쓰게 함(두 번째는 통과시키고 기록) · 예외 = 코드 블록·인용·경로·식별자를 빼고 설명 문장만 잰다(별도 끄기 장치 없음). 남은 것: 기준 비율(구현 때 실측으로 정함).
- **착수 전 확인할 것**: 하네스 정책·훅 변경이라 높음 stakes. harness 저장소 `docs/plans/`에 새 명세부터. 사용자는 하네스 문서를 한국어로 유지하기로 했다("한국어로 보는 게 나을 것 같긴 한데", 애매한 표현은 한국어본에 수정 요청).

### N6. 하네스 문서 언어별 토큰 수 측정 — 우선순위: 중간 · 사용자 요청(2026-11-17)

- **왜**: 하네스 문서를 영어로 쓸 때 절약되는 토큰을 수치로 확인. 사용자 결정 = "문서 토큰 수만 먼저"(동작 비교는 그 결과를 보고).
- **진행**: harness `docs/plans/2026-11-17/lang-token-measure/`에 영어 번역본과 측정 결과를 둔다(문서 작업 — 하네스 정책 파일은 바꾸지 않는다).

## 보류·이월

- `docs/plans/`·`docs/measurement-log.md` 커밋 여부 — public 저장소라 사용자가 정할 때까지 로컬 untracked.
- graph-nav-experiment의 `GeoLite2-City.mmdb` 52MB × 5곳 — 외부 업체 데이터베이스. 그대로 둘지 지울지 사용자 결정 대기.
- 라우팅 인덱스 — 규칙이 1건 이상 생긴 뒤.
- 하네스·에이전트 연결(배포) 방식 — 규칙이 쌓인 뒤 결정.

## 완료 이력

- 완료 → `docs/plans/2026-11-17/local-folder-move/`
- 완료 → `docs/plans/2026-11-17/org-repo-rename/`
- 완료 → `docs/plans/2026-11-17/org-profile-topics/`
- 완료 → `docs/plans/2026-11-17/org-publish/`
- 완료 → `docs/plans/2026-11-17/repo-init-readme/`
