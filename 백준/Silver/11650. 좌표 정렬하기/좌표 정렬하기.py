N = int(input())
lists = [list(map(int, input().split())) for _ in range(N)]
lists.sort(key = lambda x: (x[0], x[1]))

for i in range(len(lists)):
    print(" ".join(map(str, lists[i])))