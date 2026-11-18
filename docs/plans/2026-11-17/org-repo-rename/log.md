# log — org-repo-rename

## 타임라인

| 시각 | 사건 | 결과/결정 |
|------|------|----------|
| 18:3x | 이름 논의 | 메인 제안: `harness`·`rules`(라우팅은 저장소 안 인덱스 이름으로), `need-harness-lab` 철자 수정. 앞선 "하네스 이름 유지" 권고는 철회(개인 계정 사본이 남아 옛 링크가 유지되므로 변경 비용이 작다) |
| 18:4x | 사용자 지시 | "그럼 harness, rules로 바꾸고 철자도 수정하자" → SPEC=1 · MODE=auto |
| 18:4x | 가정 스모크 | 조직에 `harness`·`rules`·`need-harness-lab` 없음(404 × 3) |
| 18:4x | 이름 변경 3건 + 로컬 origin 변경 | 3건 모두 성공. PUBLIC·토픽·설명 유지, 로컬 fetch 성공, ahead/behind 0 |
| 18:5x | 조직 소개 글 수정 | `.github` 브랜치 `docs/rename-repos`에서 3줄 수정 → main ff 병합 → push. 원격 내용에 옛 이름 0건, 저장소 링크 6개 모두 200 |
| 18:5x | 안전선 셀프체크 | ①스모크=변경 후 조회 ②테스트 없음(설정·문서 3줄 — 사유 기록) ③diff 3줄, 의도 외 없음 ④rollback=`gh repo rename`으로 되돌림 ⑤public contract: 조직 안 옛 이름 주소는 GitHub이 새 이름으로 넘김 ⑥반증: 실험 3개·개인 계정 저장소 이름 무변경 확인(링크 200) |
| 18:5x | 사이클 마감 | NEXT.md 갱신 · CS 이슈 0건 · measurement-log 1행 |

## 리뷰 ledger

- stakes 낮음 — 셀프체크만.

## 생략한 검증

- 없음(DEBT=0).

## 완료 요약 (마감 시)

- 됐다: 조직 저장소 이름 `claude-code-harness`→`harness`, `claude-rules`→`rules`, `need-haness-lab`→`need-harness-lab`. 로컬 origin 3건, 조직 소개 글 3줄 반영.
- 그대로인 것: 로컬 폴더 이름(`claude-code-harness`, `claude-rules`, `need-haness-lab`), 저장소 안 파일(이 저장소 README 제목 `# claude-rules` 포함), 개인 계정 사본 이름.
- 이월: 저장소 안의 옛 이름 표기(README 제목·본문, 하네스 `CLAUDE.md`의 "소스 repo: claude-code-harness" 등)와 로컬 폴더 이름 — NEXT N3·N4.
