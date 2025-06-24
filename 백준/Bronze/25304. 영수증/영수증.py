X = int(input())
N = int(input())
receipt = []
for _ in range(N):
    receipt.append(list(map(int, input().split())))

for i in range(N):
    X -= receipt[i][0] * receipt[i][1]

if X == 0:
    print("Yes")
else:
    print("No")