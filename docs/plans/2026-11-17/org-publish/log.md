# log — org-publish

## 타임라인

| 시각 | 사건 | 결과/결정 |
|------|------|----------|
| 16:0x | 조직 `agent-discipline` 생성 통보(사용자) | `gh api orgs/agent-discipline` → public_repos 0, 내 role=admin |
| 16:1x | 사전 확인 | 대상 5개 로컬=원격 일치(fetch 후 ahead/behind 0), fork·star·열린 이슈 0, 태그 0. 개인 주소가 적힌 파일 약 10개(이번 범위 밖) |
| 16:2x | 인터뷰 | 원격 방식 = 개인 계정에 남기고 조직에 새로 올림 · 로컬 이동은 조사 후 · 조직 소개는 별도 · auto |
| 16:2x | need-haness-lab 추가 지시 | 조직에 올리고 실험은 Opus 에이전트에게. 메인 판단: 실험 실행은 별도 명세, 지금은 읽기 전용 조사 워커(Opus) 1건 기동 |
| 16:3x | 비용 관련 사용자 발언 | "비용은 다른 실험에서 사용한 것처럼 그대로" · "그 부분은 내가 처리할 거고, 다른 프로젝트들도 그렇게 했었잖아" — 실험 명세 입력으로 보존(메인 해석: 비용 처리는 사용자 소관) |
| 16:35 | 명세 합의 | "합의 — 5개 진행"(로컬 전용 브랜치 제외) · SPEC=1 · MODE=auto |
| 16:4x | task 01 — claude-rules 생성 + push + origin 변경 (가정 실증) | exit 0 · ref 1개 일치 · org PUBLIC·main·설명 일치 · 개인 PUBLIC 유지 · `main...origin/main` |
| 16:5x | task 02 — 4개 동일 처리 | 전부 exit 0. ref 일치: harness 8 · clean-code 21 · graph-nav 6 · compare-issue 3. org PUBLIC·기본 브랜치 main·설명 일치, 개인 계정 PUBLIC 유지, 로컬 현재 브랜치가 조직 origin 추적(ahead/behind 0) |
| 16:5x | 관측 | graph-nav-experiment push 중 GitHub 경고: `results-pilot/failed/.../GeoLite2-City.mmdb` 52.48MB(권장 50MB 초과, 거부는 아님). 개인 계정에도 이미 있던 파일 — 이번 범위 밖, NEXT 후보 |
| 16:5x | task 03 대기 | need-haness-lab 조사 워커(Opus) 미완료 — 보고 수신 후 사용자 확인 |
| 17:1x | need-haness-lab 조사 워커(Opus×1) 보고 회수 | 공개 점검: 실제 토큰·키 값 0건(이력·미커밋 모두), 50MB 초과 0건. 노출되는 것 = 커밋 author 개인 이메일(다른 5개 public 저장소와 동일), 홈 절대 경로, 세션 ID, 인증 파일 "경로". 홈 경로가 든 `harness-analysis.md`는 동결 해시 대상·baseline_sha 94cbc30 → 이력 재작성 시 동결 기준 무효. 실험 상태: cycle 1 arm1/2 첫 턴 결과 없이 중단(현 실행기로 resume 불가), arm3 명세 승인 직전 정지, Claude arm은 v1 기준·30 run 미시작 |
| 17:2x | 사용자 결정 3건 | need-haness-lab "커밋된 이력 그대로 공개" · "실험 진행자를 Opus로" · 1사이클 처리 질문에 "코덱스는 그냥 사용하지 말자. 그냥 클로드로 진행하는 방식으로 가자." + "정리해놓자" |
| 17:3x | task 03 — need-haness-lab 생성 + push + origin 추가 | 조직 PUBLIC, 기본 브랜치 `setup/payment-experiment`, 원격 SHA = 로컬 HEAD `94cbc30`, 6커밋. 미커밋·untracked 23항목은 로컬에만 남음(무변경) |
| 17:3x | 안전선 셀프체크 | ①스모크=저장소별 실행·검증 ②테스트 없음(원격 사본 생성 — 사유 기록), 불변식은 ref SHA 전수 대조로 직접 검증 ③로컬 내용 diff 없음(origin 주소만 변경) ④rollback=조직 저장소 삭제 + `git remote set-url origin <개인 주소>` ⑤public contract: 새 주소 6개 추가, 기존 주소 유지 ⑥반증: 로컬 전용 브랜치가 올라가지 않았나 → 조직 ref 수 = 개인 원격 ref 수(1·8·21·6·3)로 확인 |
| 17:3x | 사이클 마감 | NEXT.md 갱신 · CS 이슈 0건 · measurement-log 1행 |

## 리뷰 ledger

- stakes 낮음 — 셀프체크만.

## 생략한 검증

- 없음(DEBT=0).

## 완료 요약 (마감 시)

- 됐다: `agent-discipline` 조직에 public 저장소 6개 생성 — claude-rules(1) · claude-code-harness(8) · clean-code-llm-experiment(21) · graph-nav-experiment(6) · compare-issue-archive(3) · need-haness-lab(1). 괄호는 브랜치 수, 전부 원본과 SHA 일치. 로컬 6개 폴더의 origin = 조직 주소.
- diff: 저장소 내용 변경 없음(코드·문서 diff 0). 바뀐 것은 로컬 `.git/config`의 origin URL뿐.
- 그대로인 것: 개인 계정 저장소 5개(public 유지, 이 시점에서 멈춘 사본) · 로컬 폴더 위치(`/home/jun/project/<이름>`).
- 이월: 로컬 폴더 이동 · 문서 속 개인 주소 수정 · 조직 소개(.github) · graph-nav의 52MB mmdb · `need-haness-lab` 이름 오타(haness) · 실험 재개 명세.

