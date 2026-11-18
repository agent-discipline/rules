# 요구사항 명세서 (requirement-spec)

> 작성일: 2026-11-17 · 작업 폴더: `docs/plans/2026-11-17/org-profile-topics/` (기록 위치 = claude-rules. 대상은 조직 설정과 새 `.github` 저장소)

---

## 0. 요구사항 원문 (인터뷰 기록)

- 원문: "그리고 실험과 룰과 하네스는 별도 리포에서 라벨로 분리시키고, 해당 조직에 대한 소개글도 작성해야겠네."
- 앞선 결정: 조직 소개는 "이전 후 별도 작업"으로 미뤘던 항목(org-publish 인터뷰). 저장소 6개는 조직에 올라가 있다(`../org-publish/log.md`).
- 메인 해석(확인 대상): "라벨" = GitHub 저장소 토픽(topics). 저장소는 지금처럼 따로 두고, 토픽으로 하네스·규칙·실험을 구분한다.

---

## 1. 목표·대상 (필수)

`agent-discipline` 조직에서 (가) 저장소 6개에 분류 토픽을 붙이고, (나) 조직 첫 화면 소개 글(`.github` 저장소의 `profile/README.md`)과 조직 설명 문구를 올린다.

토픽 배정:

| 저장소 | 분류 토픽 | 공통 토픽 |
|---|---|---|
| claude-code-harness | `harness` | `claude-code` |
| claude-rules | `rules` | `claude-code` |
| clean-code-llm-experiment | `experiment` | `claude-code` |
| graph-nav-experiment | `experiment` | `claude-code` |
| compare-issue-archive | `experiment` | `claude-code` |
| need-haness-lab | `experiment` | `claude-code` |

- 조직 설명 문구(안): `코딩 에이전트가 정해진 절차와 규칙으로 일하게 하는 하네스와 규칙, 그리고 그 근거가 되는 실험`
- 소개 글 초안: 같은 폴더의 `profile-readme-draft.md`. 합의된 초안을 그대로 올린다.
- `.github` 저장소: public, 기본 브랜치 main, 파일은 `profile/README.md` 하나. 커밋 메시지(안) `docs: 조직 소개 추가`.

## 2. 경계·불변식 (필수)

- 저장소마다 분류 토픽은 `harness`·`rules`·`experiment` 중 정확히 하나다.
- 소개 글에는 확인된 사실만 적는다 — 각 저장소 설명은 그 저장소의 GitHub 설명·README 첫 문단에서 가져오고, 아직 없는 것(규칙 0건, need-haness-lab 본 실험 미진행)은 그렇게 적는다.
- 저장소 6개의 내용(코드·문서·브랜치)은 바꾸지 않는다. 바뀌는 것은 토픽뿐이다.
- 커밋 메시지·소개 글에 AI attribution을 넣지 않는다.

## 3. 기준소스 (필수)

조직 저장소 6개의 현재 GitHub 설명과 README 첫 문단, 이 명세의 토픽 표, 합의된 `profile-readme-draft.md`.

## 4. 금지영역 (필수)

- 개인 계정(junhyeong9812) 저장소의 토픽·설정 변경.
- 저장소 6개의 파일 수정(README 속 링크 포함), 저장소 이름 변경.
- 로컬 폴더 이동, 공통 이슈·PR 템플릿 등 `.github`의 다른 기능.
- `~/.claude/**`.

## 5. 검증 방법 (필수)

- `gh repo view agent-discipline/<이름> --json repositoryTopics` × 6 → 표와 일치.
- `gh search repos --owner agent-discipline --topic experiment` 류로 분류별 개수 확인: harness 1 · rules 1 · experiment 4.
- `gh api orgs/agent-discipline --jq .description` → 설명 문구 일치.
- `gh api repos/agent-discipline/.github/contents/profile/README.md` → 내용이 초안 파일과 동일(sha 대조).
- 소개 글 속 저장소 링크 6개가 모두 200 응답.

## 6. stakes (필수)

- 판정: 낮음 — 근거: 설정과 소개 문서 1개, 되돌리기 쉽다(토픽 제거·저장소 삭제). 공개 발행이므로 소개 글 문안은 올리기 전에 사용자 확인.

---

## 7. 자율성 (모드 — stakes와 별개 축)

- [x] auto
- [ ] lazy

## 8. load-bearing 가정 (1~2개)

- 현재 gh 인증으로 조직 설명을 바꿀 수 있다(조직 설정 권한 범위 필요) → 착수 직후 설명 변경부터 시도. 안 되면 사용자가 웹에서 직접 입력하도록 문구만 전달.

## 9. task 분해

| task | 목표 | 의존 | acceptance |
|------|------|------|-----------|
| 01 | 조직 설명 문구 설정(가정 실증) | — | §5 설명 일치 또는 "권한 없음" 보고 |
| 02 | 저장소 6개 토픽 설정 | — | §5 토픽 일치, 분류별 개수 1·1·4 |
| 03 | `.github` 저장소 생성 + `profile/README.md` push | 초안 합의 | §5 내용 동일, 링크 6개 200 |

---

## 승인 상태

- [x] 필수 6칸 전부 기입 (빈 칸 없음)
- [ ] 사용자 합의 → SPEC=1 (훅 기록 — Claude 직접 편집 금지)
- [ ] 자율성 선택 → MODE 기록
