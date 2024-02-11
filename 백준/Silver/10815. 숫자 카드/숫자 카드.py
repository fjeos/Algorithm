import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))

def bs(start, end):
    mid = N // 2
    while start <= end:
        if nums[i] == cards[mid]:
            return 1
        elif nums[i] < cards[mid]:
            end = mid - 1
            mid = (start + end) // 2
        else:
            start = mid + 1
            mid = (start + end) // 2
    return 0
            
            
for i in range(M):
    start = 0
    end = N-1
    mid = N // 2
    nums[i] = bs(start, end)
print(' '.join(map(str, nums)))