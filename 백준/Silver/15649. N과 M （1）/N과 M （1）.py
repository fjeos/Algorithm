import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def dp():    
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dp()
            result.pop()
        
dp()