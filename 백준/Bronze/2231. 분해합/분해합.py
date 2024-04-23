N = int(input())
answer = 0

for k in range(N):
    summ = k
    for j in range(len(str(k))):
        summ += int(str(k)[j])
    if summ == N:
        answer = k
        break

print(answer)
