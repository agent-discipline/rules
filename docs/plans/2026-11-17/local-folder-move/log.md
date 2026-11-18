# log — local-folder-move

> 시각 주의: 같은 날 앞선 작업 폴더(org-publish 후반, org-profile-topics, org-repo-rename)의 log에 적은 17:1x~18:5x는 실제 시계보다 앞선 추정값이었다. 이 log의 17:06은 `date`로 확인한 값이고, 그 작업들은 모두 17:06 이전에 끝났다. 순서는 맞다.

## 타임라인

| 시각 | 사건 | 결과/결정 |
|------|------|----------|
| — | 사전 조사 | 같은 파일시스템 · worktree 각 1개 · 실행 중 참조 없음 · `deploy.sh`는 자기 위치 기준 · 옛 경로 참조 = codex 설정 2건, need-haness-lab `prepare.py:36`·`SOURCE.json`, clean-code 테스트 문자열 2곳, 다른 프로젝트 `settings.local.json` 2곳, Claude Code 경로 기준 폴더 3개 |
| — | 인터뷰 4문항 | 바로가기 없이 옮김 · 기억만 복사 · README만 · codex 새 경로 추가. 사용자: "이번 세션 정보는 agent-discipline으로 옮기고 여기서 하네스를 킨 형태로" → claude-rules 이동과 세션 기록 복사는 세션 종료 후 스크립트로 |
| — | 명세 합의 | "합의 — 리뷰 생략하고 진행" (stakes 중간, 듀얼 리뷰 생략은 사용자 확인) · SPEC=1 · MODE=auto |
| — | task 01 — baseline | 5개 저장소 스냅샷(HEAD·브랜치·status 줄 수·origin·추적 파일 수). 하네스 `hooks/tests/run.sh` 261 passed. clean-code 테스트 2파일 86 passed |
| — | task 02 — 하네스 이동(가정 실증) | `claude-code-harness` → `agent-discipline/harness`. HEAD·status 동일, fetch 성공, 훅 테스트 261 passed(이동 전과 동일) |
| — | task 03 — 4개 이동 | need-haness-lab → `need-harness-lab`, 실험 3개는 같은 이름. 옛 위치 5곳 없음 확인. 전후 스냅샷 diff 0(미커밋 23항목 포함), 5곳 fetch 성공, clean-code 테스트 86 passed |
| — | task 04 — codex 설정 | 백업 `~/.codex/config.toml.bak-20261117-folder-move` 생성 후 새 경로 2건 추가. diff는 추가 6줄뿐, 항목 수 97 → 99, TOML 파싱 성공 |
| — | task 04 — 기억 복사 | 하네스 13개 → `-home-jun-project-agent-discipline-harness/memory`, need-haness-lab 3개 → `-home-jun-project-agent-discipline-need-harness-lab/memory`. 파일 수·체크섬 일치, 원본 유지 |
| — | task 05 — README | rules README 3줄(제목, 절 제목, 표 머리의 이름·링크), harness README 2줄(복제 안내). 각각 `docs/rename-readme` 브랜치 → main ff 병합 → push. 원격 README에서 반영 확인 |
| 17:06 | task 06 — 마무리 스크립트 | `/home/jun/project/agent-discipline/finish-move.sh` 작성, `bash -n` 통과. 실행은 사용자(세션 종료 후) |
| 17:06 | 안전선 셀프체크 | ①스모크=이동 후 fetch·테스트 재실행 ②테스트: 하네스 261·clean-code 86 전후 동일, 불변식(저장소 상태 동일)은 스냅샷 diff 0으로 직접 검증 ③diff: README 5줄 + 설정 6줄, 의도 외 없음 ④rollback=`mv`로 되돌림 + 설정 백업 복원 ⑤public contract: README 문구뿐 ⑥반증: 옛 경로에 기대는 실행물이 남았나 → need-harness-lab `prepare.py:36`이 남음(금지영역, 실험 준비에서 처리 — 그 스크립트를 지금 실행하면 실패한다) |
| 17:06 | 사이클 마감 | NEXT.md 갱신 · CS 이슈 0건 · measurement-log 1행 |
| 17:1x | 사용자가 마무리 스크립트 실행 후 조직 폴더에서 세션 재개 | `/home/jun/project/claude-rules` 없음, `agent-discipline/rules` 존재(HEAD 2379296, origin 조직, status 동일). 세션이 `--resume`으로 이어졌고(같은 세션 ID), 조직 폴더 기준 기억(`MEMORY.md`)이 세션 시작 시 로드됨. 게이트 상태는 새 폴더에서 UNSET으로 초기화 |

## 리뷰 ledger

- stakes 중간이나 듀얼 리뷰 생략 — 사유: 리뷰할 코드 diff가 README 5줄·설정 추가 6줄뿐. 사용자 확인: "합의 — 리뷰 생략하고 진행".

## 생략한 검증

- ~~마무리 스크립트의 실제 실행~~ — 해소: 사용자 실행, 결과 확인(타임라인 마지막 행).
- ~~옮긴 세션 기록이 새 폴더에서 `--resume`으로 이어지는지~~ — 해소: 같은 세션 ID로 재개됨.
- ~~조직 폴더 기준 기억이 읽히는지~~ — 해소: 세션 시작 시 로드됨.
- 저장소별 새 경로(`agent-discipline/harness`, `need-harness-lab`)에서 세션을 열었을 때 복사한 기억이 읽히는지 — 그 폴더에서 세션을 열어야 확인 가능. 미확인.

## 완료 요약 (마감 시)

- 됐다: 로컬 폴더 5개가 `/home/jun/project/agent-discipline/` 아래로 이동(harness · need-harness-lab · clean-code-llm-experiment · graph-nav-experiment · compare-issue-archive). codex 신뢰 경로 2건 추가, 기억 복사 2건, README 2개 수정·발행.
- diff(실파일 기준): rules `README.md` 1·14·16행, harness `README.md` 159·160행 — 내용은 타임라인 task 05와 각 저장소 커밋 참조.
- 남음: `claude-rules` 폴더 이동과 세션 기록 복사(마무리 스크립트, 사용자 실행). 위 "생략한 검증" 3건.
- 이월: need-harness-lab `prepare.py`·`SOURCE.json`의 하네스 옛 경로, 다른 프로젝트 권한 설정의 옛 경로, 하네스 정책 파일의 옛 이름 표기, 실험 저장소 문서 속 개인 계정 링크.
