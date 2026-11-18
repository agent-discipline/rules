# 요구사항 명세서 (requirement-spec)

> 작성일: 2026-11-17 · 작업 폴더: `docs/plans/2026-11-17/local-folder-move/` (기록 위치 = 이 저장소. 대상은 로컬 폴더 6개, 홈 설정 2곳, README 2개)

---

## 0. 요구사항 원문 (인터뷰 기록)

- 원문: "로컬 폴더 이동이랑 옛 이름 정리부터 진행하자" · "이번 세션 정보는 /home/jun/project/agent-discipline 여기로 옮기고 여기서 하네스를 킨 형태로 수정해야 된다는 거네."
- 앞선 결정: 로컬 폴더는 조직 폴더 아래로 모은다("프로젝트들도 별도 조직 폴더 내로 이전", "원격 먼저, 로컬은 조사 후"). 조직 저장소 이름은 `harness`·`rules`·`need-harness-lab`.
- Q/A:
  - 옛 위치 바로가기 → "바로가기 없이 옮김"
  - Claude Code 기억·세션 기록 → "기억만 새 경로로 복사"
  - 옛 이름 정리 범위 → "README만"
  - Codex 설정 → "새 경로를 추가"
- 조사로 확인한 사실(2026-11-17):
  - 6개 폴더와 `agent-discipline/`은 같은 파일시스템이다(이동 = 이름 변경). 6개 모두 git worktree 1개, 실행 중 프로세스·컨테이너 참조 없음.
  - 하네스 `hooks/deploy.sh`는 자기 위치 기준(`BASH_SOURCE`)으로 동작한다.
  - `~/.claude/projects/`에 경로 기준 폴더가 있다: 하네스(세션 10, 기억 13), need-haness-lab(세션 1, 기억 3), claude-rules(세션 1, 기억 0).
  - `~/.codex/config.toml`에 `/home/jun/project/claude-code-harness`, `/home/jun/project/need-haness-lab`이 신뢰 경로로 등록돼 있다.
  - need-haness-lab `payment-settlement/codex/scripts/prepare.py:36`과 `harness-source/SOURCE.json`(codex·claude 양쪽)이 하네스 옛 경로를 적고 있다.
  - clean-code-llm-experiment 테스트 2개에 자기 옛 경로 문자열이 있다(`experiment/runner/tests/test_blind_events.py:327`, `test_blind_runner.py:87`).
  - 다른 프로젝트의 `.claude/settings.local.json`(resume, dev-questions)에 하네스 옛 경로 권한 항목이 있다.
  - 이 세션은 `/home/jun/project/claude-rules`에서 실행 중이고 게이트 상태파일도 그 아래에 있다.

---

## 1. 목표·대상 (필수)

로컬 폴더를 `/home/jun/project/agent-discipline/` 아래로 모으고, 저장소 이름과 같은 폴더 이름을 쓴다. 옛 위치에는 아무것도 남기지 않는다.

| 지금 | 옮긴 뒤 | 시점 |
|---|---|---|
| `project/claude-code-harness` | `agent-discipline/harness` | 이번 작업 |
| `project/need-haness-lab` | `agent-discipline/need-harness-lab` | 이번 작업 |
| `project/clean-code-llm-experiment` | `agent-discipline/clean-code-llm-experiment` | 이번 작업 |
| `project/graph-nav-experiment` | `agent-discipline/graph-nav-experiment` | 이번 작업 |
| `project/compare-issue-archive` | `agent-discipline/compare-issue-archive` | 이번 작업 |
| `project/claude-rules` | `agent-discipline/rules` | **세션 종료 후** — 마무리 스크립트를 사용자가 실행 |

함께 하는 것:
- (가) `~/.codex/config.toml`에 새 경로 2건(`.../agent-discipline/harness`, `.../agent-discipline/need-harness-lab`)을 `trust_level = "trusted"`로 추가. 기존 항목은 둔다.
- (나) Claude Code 기억 복사: 하네스·need-haness-lab의 `memory/`를 새 경로 기준 폴더로 복사. 원본은 둔다.
- (다) README 2개 수정: rules README(제목 `# rules`, 하네스 이름·링크를 조직의 `harness`로), harness README의 복제 안내 2줄(`git clone` 주소와 `cd` 폴더명).
- (라) 마무리 스크립트 `agent-discipline/finish-move.sh` 작성: `claude-rules`를 `agent-discipline/rules`로 옮기고, 이 세션의 기록 파일을 `/home/jun/project/agent-discipline` 기준 폴더로 복사한다.

## 2. 경계·불변식 (필수)

- 옮기기 전후로 각 저장소의 HEAD, 현재 브랜치, `git status --short` 출력, origin 주소가 같다.
- 홈 설정은 추가·복사만 한다 — 기존 항목·원본 파일을 지우거나 고치지 않는다. `config.toml`은 수정 전 백업 사본을 만든다.
- 과거 작업 기록(`docs/plans`, `archive`)과 실험 결과물 속 옛 경로·옛 이름은 고치지 않는다.
- README 수정은 저장소마다 브랜치에서 커밋하고 main으로 fast-forward 병합한다. AI attribution 없음.

## 3. 기준소스 (필수)

이 명세 §1의 이동 표와 조직 저장소의 현재 이름(`gh repo view agent-discipline/<이름>`).

## 4. 금지영역 (필수)

- `~/.claude/**` 중 `projects/<새 경로 폴더>/memory/` 복사 대상 외 전부(정책 파일·훅·기존 프로젝트 폴더 수정 금지).
- need-harness-lab의 `prepare.py`·`SOURCE.json`·`harness-analysis.md` — 동결 해시 대상이거나 출처 기록이다. 실험 준비 작업에서 다룬다.
- 다른 프로젝트의 설정(resume, dev-questions의 `settings.local.json`), IDE 설정.
- 하네스 정책 파일(`CLAUDE.md`·`core.md` 등)의 옛 이름 표기, README 안의 실험 저장소 개인 계정 링크.
- 개인 계정 저장소.

## 5. 검증 방법 (필수)

- 이동 전후 스냅샷 대조: 저장소별 `HEAD` SHA · 브랜치 · `git status --short` 줄 수 · origin 주소 · 파일 수.
- 옛 위치 5곳이 존재하지 않고 새 위치 5곳에서 `git fetch`가 성공한다.
- 하네스: 새 위치에서 `hooks/tests/run.sh` 실행 결과가 이동 전과 같다.
- clean-code-llm-experiment: 옛 경로 문자열이 있는 테스트 2개를 이동 전후로 실행해 결과가 같다.
- `codex` 설정: 새 항목 2건 존재, 기존 항목 수 불변, 백업 파일과의 diff가 추가 줄뿐.
- 기억: 새 폴더의 파일 수·체크섬이 원본과 같다.
- README: 조직 원격의 README에 수정이 반영되고 의도한 줄만 바뀌었다(diff 확인).
- 마무리 스크립트: `bash -n` 문법 검사와 내용 검토(실행은 사용자).

## 6. stakes (필수)

- 판정: 중간 — 근거: 폴더 이동 자체는 되돌리기 쉽지만(다시 `mv`), 바로가기를 남기지 않으므로 옛 경로에 기대는 것이 바로 깨지고, 홈 디렉터리의 개인 설정 2곳을 건드린다. 하네스 규칙상 중간은 듀얼 1패스 리뷰 대상이나, 이번 변경은 코드 diff가 README 4~5줄과 설정 추가 2건뿐이라 **리뷰 대상 diff가 사실상 없다 — 듀얼 리뷰는 생략하고 §5의 이동 전후 대조로 대신할 것을 제안한다(생략은 사용자 확인 필요).**

---

## 7. 자율성 (모드 — stakes와 별개 축)

- [x] auto
- [ ] lazy

## 8. load-bearing 가정 (1~2개)

- 폴더를 옮겨도 git 저장소와 하네스 훅 테스트가 그대로 동작한다 → 가장 작은 것(compare-issue-archive가 아니라 테스트가 있는 하네스)을 먼저 옮겨 실증한다.
- Claude Code의 경로 기준 폴더 이름 규칙이 "경로의 `/`를 `-`로 바꾼 것"이다 → 기존 폴더 이름(`-home-jun-project-claude-code-harness`)으로 확인됨. 새 폴더에서 기억이 실제로 읽히는지는 새 세션에서만 확인 가능(이번 작업에서는 미확인으로 남는다).

## 9. task 분해

| task | 목표 | 의존 | acceptance |
|------|------|------|-----------|
| 01 | 이동 전 스냅샷 + 하네스·clean-code 테스트 baseline | — | 스냅샷 파일 기록 |
| 02 | 하네스 이동(가정 실증) | 01 | §5 하네스 항목 통과 |
| 03 | 나머지 4개 이동 | 02 | §5 대조 통과 |
| 04 | codex 설정 추가 · 기억 복사 | 03 | §5 설정·기억 항목 통과 |
| 05 | README 2개 수정 → 커밋 → push | 03 | §5 README 항목 통과 |
| 06 | 마무리 스크립트 작성 + 사용자 안내 | 03 | 문법 검사 통과, 안내 전달 |

---

## 승인 상태

- [x] 필수 6칸 전부 기입 (빈 칸 없음)
- [ ] 사용자 합의 → SPEC=1 (훅 기록 — Claude 직접 편집 금지)
- [ ] 자율성 선택 → MODE 기록
