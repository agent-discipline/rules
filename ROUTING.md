# 라우팅 인덱스

지금 하려는 일에 맞는 규칙 문서를 찾는 표다. 에이전트는 이 문서만 항상 읽고, 해당하는 규칙 문서는 그 일을 할 때 읽는다.

## 읽는 법

1. 아래 표에서 지금 하려는 일에 해당하는 줄을 찾는다.
2. "먼저 읽을 것"을 읽고, 이어서 "유형 문서"를 읽는다.
3. 유형 문서의 "예외" 절은 공통 원칙의 기본값보다 우선한다.
4. 해당하는 줄이 없으면 "먼저 읽을 것"만 따른다.

## 문서를 쓸 때

표는 쓰려는 문서의 종류별로 읽을 규칙 문서를 보여 준다.

| 쓰려는 문서 | 먼저 읽을 것 | 유형 문서 |
|---|---|---|
| 요구사항 명세서, 작업 log, NEXT, 측정 로그 | 해당 없음 | [writing/work-records.md](writing/work-records.md) |
| 학습 노트, 이슈 카드, 실험 기록, 독후감 | [writing/principles.md](writing/principles.md) | writing/study-notes.md (작성 예정) |
| 소스 코드 해설서 | [writing/principles.md](writing/principles.md) | writing/walkthroughs.md (작성 예정) |
| 유스케이스, ADR, 절차서, 아키텍처 뷰, 인수인계 문서 | [writing/principles.md](writing/principles.md) | writing/design-docs.md (작성 예정) |
| README, 커밋 메시지, 이슈, PR 본문 | [writing/principles.md](writing/principles.md) | writing/collaboration.md (작성 예정) |
| 그 밖에 사람이 읽을 문서 | [writing/principles.md](writing/principles.md) | 해당 없음 |

한국어 문서를 다 쓴 뒤에는 [writing/wording-table.md](writing/wording-table.md)의 왼쪽 열 낱말로 검색해 어색한 표현이 남았는지 확인한다.

문서에 흐름, 구조, 상태 변화, 전후 대비가 들어가면 유형과 상관없이 [writing/diagrams.md](writing/diagrams.md)를 함께 읽는다.

작업 기록은 사람이 읽기 좋게 다듬는 문서가 아니라 작업의 원본이라서 공통 원칙의 형식 기본값을 따르지 않는다. 그래서 "먼저 읽을 것"이 없다.

## 규칙 문서의 형식

모든 규칙 문서는 같은 네 칸으로 쓴다.

- **언제 적용하나**: 이 문서를 읽어야 하는 상황과 알아보는 신호
- **규칙**: 무엇을 어떻게 하는가. 규칙마다 출처 표시가 붙는다
- **예외**: 공통 기본값과 다르게 하는 부분
- **출처**: 원본 문서의 위치. 원본은 각 저장소에 그대로 있다
