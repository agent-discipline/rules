# 요구사항 명세서 (requirement-spec)

> 작성일: 2026-11-17 · 작업 폴더: `docs/plans/2026-11-17/org-repo-rename/` (기록 위치 = 이 저장소. 대상은 조직 저장소 3개의 이름과 `.github` 소개 글)

## 0. 요구사항 원문 (인터뷰 기록)

- 원문: "그냥 하나씩 harness/rules로 명명하는 게 더 나은가? (…) rules이 나을지 아니면 (…) 라우팅룰?" → 메인 제안(이름 표 + 범위: 조직 저장소 이름 변경, 로컬 origin 주소 변경, 조직 소개 글의 링크·이름 수정. 로컬 폴더 이름은 폴더 이동 작업 때) → "그럼 harness, rules로 바꾸고 철자도 수정하자"
- 합의 근거: 위 사용자 발언이 메인이 제시한 이름 표와 범위에 대한 진행 지시다. 자율성은 오늘 앞선 세 작업과 같은 auto.

## 1. 목표·대상 (필수)

`agent-discipline` 조직에서 `claude-code-harness`→`harness`, `claude-rules`→`rules`, `need-haness-lab`→`need-harness-lab`으로 이름을 바꾸고, 로컬 3개 폴더의 origin 주소와 조직 소개 글(`.github/profile/README.md`)의 해당 이름·링크를 새 이름으로 맞춘다.

## 2. 경계·불변식 (필수)

저장소 내용·브랜치·토픽·설명·공개 범위는 변하지 않는다. 로컬 폴더 이름과 위치는 그대로다. 개인 계정 저장소는 건드리지 않는다.

## 3. 기준소스 (필수)

이 명세 §1의 이름 대응 3건.

## 4. 금지영역 (필수)

개인 계정 저장소 · 실험 3개(clean-code-llm-experiment, graph-nav-experiment, compare-issue-archive)의 이름 · 저장소 6개 안의 파일(README 제목·링크 포함 — 별도 작업) · 로컬 폴더 이동/이름 변경 · `~/.claude/**`.

## 5. 검증 방법 (필수)

- `gh repo view agent-discipline/<새 이름>` × 3 → 존재, PUBLIC, 토픽·설명 유지.
- 로컬 3개 폴더 `git remote get-url origin` = 새 주소, `git fetch` 성공, `git status -sb` ahead/behind 0.
- 조직 소개 글 원격 내용에 옛 이름 0건, 저장소 링크 6개 모두 200.

## 6. stakes (필수)

- 판정: 낮음 — 근거: 이름 변경은 되돌릴 수 있고 GitHub이 조직 안 옛 이름을 새 이름으로 넘겨 준다. 내용 변경은 소개 글 3줄.

## 7. 자율성

- [x] auto

## 8. load-bearing 가정

- 조직에 `harness`·`rules`·`need-harness-lab`이라는 저장소가 아직 없다 → 착수 직후 조회.

## 승인 상태

- [x] 필수 6칸 전부 기입
- [x] 사용자 합의(위 §0 발언) → SPEC=1은 set-state로 기록
- [x] 자율성 auto
