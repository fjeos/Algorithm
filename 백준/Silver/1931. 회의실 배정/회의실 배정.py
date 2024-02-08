import sys
input = sys.stdin.readline

lists = [(list(map(int, input().split()))) for _ in range(int(input()))]
lists.sort(key = lambda x:(x[1],x[0]))

count = 0
start = 0
for i in lists:
    if i[0] >= start:
        count += 1
        start = i[1]
    
print(count)