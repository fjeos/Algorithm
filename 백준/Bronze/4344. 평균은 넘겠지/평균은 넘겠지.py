for _ in range(int(input())):
    count = 0
    sum1 = 0
    result = 0
    a = list(map(int, input().split()))
    for i in range(1, a[0] + 1):
        sum1 += a[i]
    avg = sum1 / a[0]
    for j in range(1 ,a[0] + 1):
        if a[j] > avg:
            count += 1
    result = count / a[0] * 100
    
    print("%.3f%%"%result)