N = int(input())
cards,lists = [],[]
winner, maxi = 0, 0

for i in range(N):
    cards.append(list(map(int, input().split())))

for k in range(N):
    setList = set()
    for i in range(5):
        for j in range(5):
            if j == i:
                continue
            for m in range(5):
                if m == j or m == i:
                    continue
                setList.add((cards[k][i] + cards[k][j] + cards[k][m])%10)
    lists.append(max(setList))

for i in range(len(lists)):
    if lists[i] >= maxi:
        maxi = lists[i]
        winner = i+1
        
print(winner)