N = int(input())
result = 0
while N % 5 != 0:
        N -= 3
        result += 1
        if N < 0:
            count = -1
            break
if N >= 0:
    result += N // 5
else:
    result = -1
print(result)