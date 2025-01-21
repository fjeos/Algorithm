N, L = map(int, input().split())
hlist = list(map(int, input().split()))
hlist.sort()
for i in range(N):
    if hlist[i] <= L:
        L += 1
print(L)