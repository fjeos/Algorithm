n, k = int(input()), int(input())
cards = [input() for _ in range(n)]
setList = set()

if k == 2:
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            setList.add(cards[i] + cards[j])
    
elif k == 3:
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for m in range(n):
                    if m == j or m == i:
                        continue
                    setList.add(cards[i] + cards[j] + cards[m])
    
else:
    for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for m in range(n):
                    if m == j or m == i:
                        continue
                    for p in range(n):
                        if p == m or p == j or p == i:
                            continue
                        setList.add(cards[i] + cards[j] + cards[m] + cards[p])
    
print(len(setList))