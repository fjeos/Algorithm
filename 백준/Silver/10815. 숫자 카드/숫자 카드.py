import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards = set(cards)
M = int(input())
nums = list(map(int, input().split()))
result = []
for i in range(M):
    if nums[i] in cards:
        result.append(1)
    else:
        result.append(0)
        
print(' '.join(map(str, result)))
    