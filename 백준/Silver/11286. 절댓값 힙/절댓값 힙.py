import heapq, sys

input = lambda: sys.stdin.readline().rstrip()

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(x), x))