# log — writing-rules

## 타임라인

| 시각 | 사건 | 결과/결정 |
|------|------|----------|
| 2026-11-17 오후 | 탐색 — explorer(Sonnet) 4건 기동, 3건 회수(1건은 검색 도구 타임아웃으로 무산 → 메인이 `find`로 후보를 뽑아 재위임) | 하네스 · study-note · 프로젝트별 규칙 파일 보고. 출처 지도는 `docs/plans/NEXT.md` N1 |
| 17:2x | 인터뷰 | 유형 전부 · 그림 기본 ASCII(설계 문서만 Mermaid) · 기본값 하나 + 유형별 예외 · 특수 기호는 깨지지 않으면 허용 · 개인 문서는 일반화한 규칙만(이력서·지원동기는 별도 대화) · 구조와 네 칸 형식 "이대로" · auto + 묶음별 확인 |
| 17:33 | 명세 합의 | "합의 — 진행" · SPEC=1 · MODE=auto · stakes 낮음 |
| 17:3x~ | 1차 묶음 원문 직접 읽기 | `study-note-guide.md` 322~343·813~990·1066~1093·1179~1186 · `writing-methodology.md` 전문 · `reference/writing/README.md` 전문 · `render-rules.md` 70~104 · `templates/project-issue.md` 1~12·58~70 · `cs/README.md` 36~62 · jun-bank `phase3/05` 발췌·`phase2/03` 160~204 · `handover-template.md` 1776~1791 · 하네스 템플릿 4개 전문 · `issue-archive.md` 25~36. `issue/authoring-guide.md` 전문(앞서 읽음) |
| 17:5x | 가정 실증 | 네 칸 형식 + 120줄 상한에 담김 — principles 86줄, diagrams 75줄, work-records 77줄, ROUTING 36줄 |
| 17:5x | task 01 — 1차 묶음 작성(브랜치 `docs/writing-rules`, 미커밋) | 형식 점검: 네 칸 제목 3/3 문서 · 링크 대상 3개 존재 · 개인정보 패턴 0건. 중복 1건(코드 인용 복사 규칙이 principles 3번과 work-records 17번에 중복) → 17번을 참조형으로 고침 |
| 17:5x | 출처 대조 | 규칙 항목마다 위 읽은 범위에서 해당 문장 확인. 메인이 범위를 넓힌 것 1건: diagrams 11~15번(화살표는 주장이다)은 원본에서 "원문을 다시 풀어 쓰는 문서" 한정 규칙인데 그림 일반 규칙으로 옮겼다 — 사용자 확인 대상 |
| 2026-11-18 17:02 | principles.md에 "낱말" 절(규칙 19~26, 예시 표) + 판정 1줄 + 출처 1줄 추가 (사용자 요청: 한국어 문서의 외래어 처리 규칙, 내용 추가만) | 초안. 사용자가 읽고 다듬을 예정, 커밋 안 함 |
| 2026-11-18 저녁 | writing/wording-table.md 신설(유형 3개 65줄 + 바꾸지 않는 말) + principles, ROUTING에 가리킴 1줄씩 (사용자 요청: 매칭표) | 초안, 미커밋. 출처는 resume 문서 검토분. lab, agent-discipline, study-note는 반영 전 |

## 리뷰 ledger

- stakes 낮음 — 셀프체크 + 묶음별 사용자 검토.

## 생략한 검증

- 없음.

## 완료 요약 (마감 시)

