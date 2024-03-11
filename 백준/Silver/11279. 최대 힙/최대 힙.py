import heapq, sys
input = lambda: sys.stdin.readline().rstrip()
maxHeap = []
for _ in range(int(input())):
    command = int(input())
    if command == 0 and maxHeap:
        print(heapq.heappop(maxHeap)[1])
    elif command == 0 and not maxHeap:
        print(0)
    else:
        heapq.heappush(maxHeap, (-command, command))