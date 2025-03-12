import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
belt = belt + belt[:k-1]  # 원형으로 처리하기 위해 필요한 부분만 추가

# 슬라이딩 윈도우 구현
answer = 0
counter = defaultdict(int)


# 초기 윈도우 설정
for i in range(k):
    counter[belt[i]] += 1

# 쿠폰 고려한 초기값 계산
if c not in counter:
    answer = len(counter) + 1
else:
    answer = len(counter)

# 슬라이딩 윈도우 이동
for i in range(k, n+k-1):
    # 이전 초밥 제거
    counter[belt[i-k]] -= 1
    if counter[belt[i-k]] == 0:
        del counter[belt[i-k]]
    
    # 새 초밥 추가
    counter[belt[i]] += 1
    
    # 현재 윈도우에서 가능한 최대 종류 계산
    current = len(counter)
    if c not in counter:
        current += 1
        
    answer = max(answer, current)

print(answer)