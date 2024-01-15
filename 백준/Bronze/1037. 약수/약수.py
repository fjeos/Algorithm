N = int(input())
listt = list(map(int, input().split()))
listt.sort()
print(listt[0] * listt[-1])