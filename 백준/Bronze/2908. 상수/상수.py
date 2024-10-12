a = list(map(str, input().split()))
s, b = '', ''
for j in range(2, -1, -1):
    s += a[0][j]
for i in range(2, -1, -1):
    b += a[1][i]
print(max(int(s), int(b)))