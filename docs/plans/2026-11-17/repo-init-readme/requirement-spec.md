# 요구사항 명세서 (requirement-spec)

> 작성일: 2026-11-17 · 작업 폴더: `docs/plans/2026-11-17/repo-init-readme/`

---

## 0. 요구사항 원문 (인터뷰 기록)

- 원문: "이 폴더를 이닛하고 리드미부터 만들면서 하나씩 구현하려고 해. (…) claude-code-harness가 클로드가 절차에 맞게 일하게 만드는 하네스라면, 이번에 만드는 건 각 문제상황에 대해 규칙을 만들어 A라는 문제에는 a 방식, B라는 문제에는 b 방식을 사용하도록 접근방식과 해결방식을 정리하고, 이를 바탕으로 에이전트들이 작업하게 하여 통일성과 규칙성을 갖게 하려는 것."
- 추가 지시(진행 중 수신):
  - "해당 커밋은 어제자 저녁 11시에 커밋한 기록으로 메타데이터 작성도 부탁해."
  - "프로젝트는 private이 아닌 public으로 하고 프로젝트 설명도 부탁해."
- Q/A:
  - 문제 영역 → 코딩 작업 유형 · 설계·아키텍처 결정 · 특정 기술 스택 문제 · 비코딩 작업 (4개 전부)
  - 전달 형태 → 라우팅 인덱스 + 조건부 문서
  - 규칙 원천 → "너랑 이야기하면서 각 방법론을 정립하면서 문서화를 하려고 하는 거라, 둘 다 활용하는 1번인데 굳이 외부 문헌보단 너가 3번처럼 각 방법론을 알려줄 거고, 거기에 내가 이게 맞는지 아닌지 고민해보면서 풀어나갈 예정"
  - 첫 작업 범위 → git init + README만
  - 하네스와의 관계 → 독립 repo, 연결은 나중에
  - git 범위 → init + 커밋 + GitHub 원격
  - README 내용 → 확정된 것만
  - 자율성 → auto

---

## 1. 목표·대상 (필수)

`/home/jun/project/claude-rules`를 git 저장소로 초기화하고, 확정된 내용만 담은 한국어 `README.md`를 첫 커밋으로 올린 뒤 GitHub public 저장소 `junhyeong9812/claude-rules`로 발행한다.

- README 구성(확정된 것만): ①취지 ②claude-code-harness와의 차이·관계(절차 vs 문제별 접근법 / 독립 repo, 연결은 추후 결정) ③다루는 문제 영역 4가지 ④규칙 정립 방식(대화로 방법론 제안 → 사용자 검토·판단 → 문서화) ⑤전달 형태(라우팅 인덱스 + 조건부 문서) ⑥현재 상태(규칙 0건, 구조·형식 미정)
- 첫 커밋 파일: `README.md` + `.gitignore`(`.claude/` 제외용 — 세션 상태파일·로컬 설정이 public repo에 올라가지 않게)
- 커밋 메타데이터: author date·committer date 모두 `2026-11-16 23:00:00 +0900`
- 커밋 메시지(안): `docs: 프로젝트 취지를 담은 README 추가`
- GitHub 설명(안): `문제 유형별 접근·해결 방식을 규칙으로 정리해, 에이전트가 일관된 방식으로 작업하게 하는 규칙 모음`

## 2. 경계·불변식 (필수)

- README에는 인터뷰에서 확정된 내용만 적는다 — 디렉토리 구조·규칙 형식·로드맵·배포 방식은 적지 않는다(미정임을 1행으로만 표기).
- 첫 커밋에는 `README.md`·`.gitignore` 2파일만 들어간다. `.claude/`와 `docs/plans/`는 포함하지 않는다(docs는 로컬에 untracked로 유지 — public 공개 여부는 별도 결정).
- 커밋 메시지·GitHub 설명·README에 AI attribution을 넣지 않는다.
- 기본 브랜치는 `main`.

## 3. 기준소스 (필수)

이 명세서 §0의 사용자 답변 원문. 하네스와의 대비 서술은 `/home/jun/project/claude-code-harness/README.md` 실파일 기준.

## 4. 금지영역 (필수)

- `/home/jun/project/claude-code-harness/**`, `~/.claude/**` — 읽기만, 수정 금지.
- `.claude/lazymode/` 상태파일 직접 편집 금지(set-state 경유만).
- 규칙 문서·템플릿·인덱스·배포 스크립트 등 README 외 산출물 생성 금지(다음 작업).

## 5. 검증 방법 (필수)

- `git log -1 --format='%ad | %cd | %s' --date=iso` → 두 날짜 모두 `2026-11-16 23:00:00 +0900`
- `git show --stat HEAD` → 파일 2개(README.md, .gitignore)만
- `git status --short` → `.claude/` 미노출(ignore 동작), `docs/`만 untracked
- push 후 `gh repo view junhyeong9812/claude-rules --json visibility,description,defaultBranchRef` → PUBLIC·설명 일치·main
- README diff self-review — §2 "확정된 것만" 위반 없는지

## 6. stakes (필수)

- 판정: 낮음 — 근거: 문서 1개 + ignore 1개, 코드·데이터 없음. 다만 public 발행은 외부 노출이라 저장소 생성·push 직전에 각각 사용자 확인(stakes 무관 안전선).

---

## 7. 자율성 (모드 — stakes와 별개 축)

- [x] auto
- [ ] lazy

## 8. load-bearing 가정 (1~2개)

- GitHub 계정 `junhyeong9812`에 `claude-rules`라는 이름의 저장소가 아직 없다 → 착수 직후 `gh repo view`로 확인.

## 9. task 분해

| task | 목표 | 의존 | acceptance |
|------|------|------|-----------|
| 01 | git init(-b main) + README.md·.gitignore 작성 | — | README가 §1 구성 6항만 포함 |
| 02 | 지정 날짜로 첫 커밋 | 01 | §5 로그·stat·status 검증 통과 |
| 03 | GitHub public 저장소 생성 + push (각각 확인 후) | 02 | §5 gh repo view 검증 통과 |

---

## 승인 상태

- [x] 필수 6칸 전부 기입 (빈 칸 없음)
- [ ] 사용자 합의 → SPEC=1 (훅 기록 — Claude 직접 편집 금지)
- [ ] 자율성 선택 → MODE 기록
