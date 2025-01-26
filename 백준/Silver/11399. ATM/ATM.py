N = int(input())
time = list(map(int, input().split()))
time.sort()

tot = 0
result = [0]
for i in range(N):
    result.append(result[i]+time[i])
print(sum(result))