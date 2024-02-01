A, X = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(A):
    if numbers[i] < X:
        print(numbers[i], end = ' ')