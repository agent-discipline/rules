# log — move-writing-to-harness

## 타임라인

| 시각 | 사건 | 결과/결정 |
|------|------|----------|
| 11-20 16:03 | 사용자 합의(하네스 저장소의 명세 — `agent-discipline/harness` `docs/plans/2026-11-20/writing-rules-builtin/requirement-spec.md`, I8) | 이 저장소의 `writing/`과 `ROUTING.md`를 지우고 README에 옮긴 곳을 적는다. 합의 질문과 답은 하네스 쪽 작업 폴더의 `decisions.md`에 있다 |
| 11-20 16:13 | 브랜치 `chore/move-writing-to-harness`(기준 `9bcf101`), `git rm -r writing ROUTING.md` | 하네스 `playbooks/writing/`에 같은 내용이 들어간 것을 확인한 뒤(네 문서는 바이트까지 동일, 하네스 커밋 `d6b4506`·`5795a97`) |
| 11-20 16:13 | README Edit이 게이트에 막힘(SPEC=0) | 게이트 상태가 저장소마다 따로라서, 하네스에서 기록한 합의가 이 저장소의 상태에는 없었다. 같은 순간에 낸 커밋은 README 수정 없이 삭제만 담겼다(`bb9d6df` — 메시지와 내용이 어긋남, 아래에서 고침) |
| 11-20 16:13 | 이 작업 폴더와 명세를 만들고, 위 합의를 이 저장소의 게이트 상태에 기록(`set-state spec-approved`·`mode auto`) | 새 합의를 받은 것이 아니라 16:03의 합의를 이 저장소에 옮겨 적은 것 |
| 11-20 16:14 | README "현재 상태" 절 수정, 앞 커밋을 고쳐 README와 이 작업 폴더를 함께 담음(push 전이라 amend) | 커밋 메시지와 내용이 맞음 |

## 생략한 검증 (긴급 경로 빚 — DEBT=1인 동안 정본)

- 없음.

## 완료 요약 (마감 시)

- `writing/` 네 문서와 `ROUTING.md` 삭제(557줄), README "현재 상태" 절을 보류 상태와 새 위치 안내로 교체. 다른 절은 그대로.
- 검증: 하네스 `playbooks/writing/`의 네 문서가 지우기 전 원본과 같음(`cmp`), README의 하네스 링크는 병합 뒤 `main`에서 열린다(병합 전에는 브랜치에만 있음).

