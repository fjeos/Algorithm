A, B = map(int, input().split())
m = int(input())
number = list(map(int, input().split()))
ten, result = [], []
total = 0

j = m-1
for i in range(m):
    ji = 1
    for k in range(i):
        ji *= A
    total += ji*number[j]
    j -= 1
    
P = total//B
result.insert(0, total%B)
while P != 0:
    result.insert(0, P%B)
    P //= B
print(' '.join(map(str, result)))