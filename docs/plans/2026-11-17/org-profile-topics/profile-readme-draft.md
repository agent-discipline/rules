# agent-discipline

코딩 에이전트가 정해진 절차와 규칙에 따라 일하게 만드는 저장소 모음.

에이전트에게 같은 일을 맡겨도 매번 다른 방식으로 접근하면 결과를 믿기 어렵다. 이 조직은 두 가지를 정한다. 하나는 **어떤 절차로 일하는가**이고, 다른 하나는 **이 문제는 어떤 방식으로 푸는가**다. 그리고 그 규칙이 실제로 효과가 있는지를 실험으로 확인한다.

## 저장소

저장소는 세 갈래로 나뉘고, 토픽으로 구분한다.

### 하네스 (`harness`)

- [claude-code-harness](https://github.com/agent-discipline/claude-code-harness): Claude Code가 인터뷰, 명세 합의, 구현, 검증, 기록의 순서를 거치도록 강제하는 규칙·훅·템플릿 패키지.

### 규칙 (`rules`)

- [claude-rules](https://github.com/agent-discipline/claude-rules): 문제 유형별 접근 방식과 해결 방식을 정리한 규칙 모음. 지금은 규칙을 정립하는 단계다.

### 실험 (`experiment`)

- [clean-code-llm-experiment](https://github.com/agent-discipline/clean-code-llm-experiment): 사람에게 좋은 설계가 LLM 코딩 에이전트에게도 좋은지를 갓 클래스와 레이어드 구조로 비교한다.
- [graph-nav-experiment](https://github.com/agent-discipline/graph-nav-experiment): 코드 지도와 네이밍·아키텍처 중 무엇이 에이전트의 토큰과 정답률을 정하는지 측정한다.
- [compare-issue-archive](https://github.com/agent-discipline/compare-issue-archive): 이슈·의사결정 기록이 코딩 에이전트에게 도움이 되는지 측정한다.
- [need-haness-lab](https://github.com/agent-discipline/need-haness-lab): 하네스 절차가 짧은 요청이나 상세 프롬프트보다 실제로 나은지 비교한다. 본 실험은 아직 진행 전이다.

## 원칙

규칙은 측정한 근거가 있을 때만 늘리거나 줄인다. 실험 저장소가 규칙 저장소와 같은 조직에 있는 이유다.
