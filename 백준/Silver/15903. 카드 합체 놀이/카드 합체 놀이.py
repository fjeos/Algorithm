import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

heapq.heapify(cards)
for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x+y)
    heapq.heappush(cards, x+y)
print(sum(cards))