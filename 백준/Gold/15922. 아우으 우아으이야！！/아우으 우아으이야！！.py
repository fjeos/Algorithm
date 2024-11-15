import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
 
x1,y1 = map(int, input().split())
 
result = 0
for i in range(N-1):
    x2,y2 = map(int, input().split())
 
    if x1 <= y2 <= y1:  # case 3
        continue
    elif x1 <= x2 <= y1 and not x1 <= y2 <= y1: # case 2
        y1 = y2
    else:   # case 1
        result += abs(y1 - x1)
        x1, y1 = x2, y2

print(result + abs(y1 - x1))