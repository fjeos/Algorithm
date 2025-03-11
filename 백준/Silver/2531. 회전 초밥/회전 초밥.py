import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

# 벨트를 2배로 늘려 원형 회전을 구현
belt += belt  

# 초기 윈도우 설정
kinds = deque(belt[:k])
unique_sushi = set(kinds)
answer = len(unique_sushi) + (1 if c not in unique_sushi else 0)

# 슬라이딩 윈도우 시작
for start in range(1, n):  # 1부터 시작
    end = start + k - 1  # 마지막 초밥 위치

    # 왼쪽 초밥 제거
    removed_sushi = kinds.popleft()
    if removed_sushi not in kinds:  # 더 이상 남아있지 않다면 제거
        unique_sushi.remove(removed_sushi)

    # 오른쪽 초밥 추가
    added_sushi = belt[end]
    kinds.append(added_sushi)
    unique_sushi.add(added_sushi)

    # 쿠폰 초밥 추가 여부 확인
    current_count = len(unique_sushi) + (1 if c not in unique_sushi else 0)
    answer = max(answer, current_count)

print(answer)
