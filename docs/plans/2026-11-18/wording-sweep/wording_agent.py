#!/usr/bin/env python3
"""agent-discipline 실험 저장소의 독자용 문서(README, docs/adr, docs/results, docs/*.md)에 쓰는 낱말 치환.
사용: wording_agent.py <파일...> [--dry]. 보호 구간과 조사 맞춤은 wording_lab.py와 같다.
실험 입력물(cases, oracle, target, target-docs, graphs, subjects, archive-v*, results*)과 작업 기록(docs/plans)에는 쓰지 않는다."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wording_lab as W
W.R = [
 (r'지엽성', '지역성'),
 (r'기준선', '베이스라인'), (r'독립 판정기', '독립 판정 스크립트'), (r'판정기', '판정 스크립트'),
 (r'문턱 잡음', '기준값 근처 잡음'), (r'문턱', '기준값'),
 (r'(\d+)칸', r'\1셀'), (r'(?<![가-힣])칸(?![가-힣])', '셀'), (r'(?<![가-힣])칸(마다|별|당)', r'셀\1'),
 (r'탐침', '프로브'),
 (r'낱말 grep으로 닿았다', '낱말 grep으로 찾았다'), (r'\)로 닿았다', ')로 찾았다'),
 (r'닿기까지', '도달하기까지'), (r'닿았다', '도달했다'), (r'닿았고', '도달했고'), (r'닿았는', '도달했는'), (r'닿는다', '도달한다'), (r'닿는', '도달하는'), (r'닿아', '도달해'), (r'닿으면', '도달하면'), (r'닿지', '도달하지'), (r'닿을', '도달할'), (r'닿은', '도달한'),
 (r'다시 훑었다', '다시 읽었다'), (r'훑는다', '스캔한다'), (r'훑은', '스캔한'), (r'훑는', '스캔하는'),
 (r'탐색 비용을 묶는다', '탐색 비용을 제한한다'),
 (r'실험장', '실험 저장소'), (r'찾히는', '찾을 수 있는'), (r'업무어', '업무 용어'),
 (r'본보기', '예시'), (r'재표본 2,000회', '재표본 추출 2,000회'),
 (r'(stderr|stdout|출력) 꼬리', r'\1 끝부분'),
 (r'쥐는 잠금', '잡는 잠금'), (r'먼저 쥐고', '먼저 잡고'), (r'쥐는 경로', '잡는 경로'),
 (r'이긴 쪽', '성공한 요청'), (r'진 쪽', '실패한 요청'), (r'진 요청', '실패한 요청'),
 (r'무음 제외 금지', '조용히 제외하지 않는다'),
]
if __name__ == '__main__':
    dry = '--dry' in sys.argv
    for p in [a for a in sys.argv[1:] if not a.startswith('--')]:
        s = open(p, encoding='utf-8').read(); t, n = W.convert(s)
        if n: print(p, n)
        if not dry and t != s: open(p, 'w', encoding='utf-8').write(t)
