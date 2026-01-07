N, M = map(int, input().split())
J = int(input())
count, start, end = 0, 1, M

for i in range(J):
    apple = int(input())
    if end >= apple and start <= apple:
        continue
    elif apple > end:
        count += apple - end
        start = apple - (M - 1)
        end = apple
    elif apple < start:
        count += start - apple
        start = apple
        end = start + (M - 1)
print(count)