import sys
input = lambda: sys.stdin.readline().rstrip()

import heapq
heap = []
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if len(heap) == 0:
            print(0)
            continue
        min_value, value = heapq.heappop(heap)
        print(value)

