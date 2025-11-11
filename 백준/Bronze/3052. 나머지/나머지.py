numbers = [int(input()) for _ in range(10)]
answer = set()
for i in range(10):
    answer.add(numbers[i] % 42)
print(len(answer))