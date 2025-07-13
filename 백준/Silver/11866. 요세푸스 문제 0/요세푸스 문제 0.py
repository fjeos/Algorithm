N, K = map(int, input().split())
numbers = [i for i in range(N)]
index = 0
print("<", end = '')
while numbers:
    if index >= len(numbers):
        index = 0
    for _ in range(K-1):
        index += 1
        if index >= len(numbers):
            index = 0
    print(numbers[index]+1, end = '')
    del numbers[index]
    if len(numbers) > 0:
        print(", ", end = '')
print(">")