N = int(input())
cur, count, i, start = 0, 0, 1, 1
while start <= N:
    cur += i
    i += 1
    if cur > N:
        while cur > N:
            cur -= start
            start += 1
    if cur == N:
        count += 1
print(count) 