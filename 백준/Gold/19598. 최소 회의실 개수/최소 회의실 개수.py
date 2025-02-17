import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

times = sorted([list(map(int, input().split())) for _ in range(int(input()))])
heap = []
count = 0
for start, end in times:
    while heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    count = max(count, len(heap))
print(count)
