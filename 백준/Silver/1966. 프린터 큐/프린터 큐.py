import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, M = map(int, input().split())
    rank = list(map(int, input().split()))
    queue = [[index, rank] for index, rank in enumerate(rank)]
    count = 0
    
    while queue:
        if queue[0][1] != max(q[1] for q in queue):
            queue.append(queue[0])
            queue.pop(0)
        elif queue[0][1] == max(q[1] for q in queue):
            count += 1
            if queue[0][0] == M:
                break
            queue.pop(0)
    
    print(count)