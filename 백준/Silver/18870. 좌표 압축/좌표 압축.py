from collections import defaultdict

N = int(input())
position = list(map(int, input().split()))
copy = sorted(list(set(position)))
dic = defaultdict(int)

for i, num in enumerate(copy):
    dic[num] = i

for i in range(N):
    print(dic[position[i]], end=' ')
