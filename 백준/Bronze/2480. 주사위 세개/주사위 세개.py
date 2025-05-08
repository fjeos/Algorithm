num = list(map(int, input().split()))
if num.count(num[0]) == 2:
    print(1000 + num[0] * 100)
elif num.count(num[1]) == 2:
    print(1000 + num[1] * 100)
elif num.count(num[0]) == 3:
    print(10000 + num[0] * 1000)
elif num.count(num[1]) == 3:
    print(10000 + num[1] * 1000)
else:
    print(max(num) * 100)