numbers = [0 for _ in range(30)]
for _ in range(28):
    numbers[int(input()) - 1] = 1
print(min(filter(lambda x: numbers[x] == 0, range(30))) + 1)
print(max(filter(lambda x: numbers[x] == 0, range(30))) + 1)