N, M = map(int, input().split())
que = []
for i in range(1, N+1):
    que.append(i)

lists = list(map(int, input().split()))
count = 0

while lists:
    if lists[0] == que[0]:
        que.pop(0)
        lists.pop(0)
        continue
        
    if que.index(lists[0]) <=  len(que)//2:
        que.append(que[0])
        que.pop(0)
        count += 1

    else:
        que.insert(0, que[-1])
        que.pop()
        count += 1

print(count)