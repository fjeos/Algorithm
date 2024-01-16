N, M = map(int, input().split())#세로, 가로

guard = []
count = 0
result = []

for _ in range(N):
    guard.append(input())
    
while True :
    if (N == 1 or M == 1) and 'X' in guard:
        result.append(0)
        break
    for i in range(N):
        if 'X' not in guard[i]:
            count += 1

    result.append(count)
    count = 0

    for i in range(M):
        hasX = False
        for j in range(N):
            #print(f'j={j}, i={i}, {guard[j][i]}')
            if guard[j][i] == 'X':
                hasX = True
                #print(hasX)
        if not hasX:
            count += 1
            #print(count)
    result.append(count)
    break

#print(result)        
print(max(result))