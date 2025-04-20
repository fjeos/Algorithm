import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

X = int(input())
sticks = []
heapq.heapify(sticks)
heapq.heappush(sticks, 64)

count = 1
while sum(sticks) != X:
    shortest_sticks = heapq.heappop(sticks)
    shortest_sticks //= 2
    if sum(sticks) + shortest_sticks >= X:
        heapq.heappush(sticks, shortest_sticks)
    else:
        heapq.heappush(sticks, shortest_sticks)
        heapq.heappush(sticks, shortest_sticks)
    
print(len(sticks))
