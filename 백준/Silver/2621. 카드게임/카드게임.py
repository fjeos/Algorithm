import sys
input = lambda: sys.stdin.readline().rstrip()

colors, numbers = [], []
for _ in range(5):
    x, y = input().split()
    colors.append(x)
    numbers.append(int(y))
numbers.sort()

# 1번 경우
if all(color == colors[0] for color in colors) and all(numbers[i + 1] == numbers[i] + 1 for i in range(4)):
    print(max(numbers) + 900)
# 2번 경우
elif numbers.count(numbers[2]) == 4:
    print(numbers[2] + 800)
# 3번 경우
elif numbers.count(numbers[2]) == 3 and numbers.count(numbers[3]) == 2:
    print(numbers[2] * 10 + numbers[3] + 700)
elif numbers.count(numbers[0]) == 2 and numbers.count(numbers[3]) == 3:
    print(numbers[3] * 10 + numbers[0] + 700)
# 4번 경우
elif all(color == colors[0] for color in colors):
    print(max(numbers) + 600)
# 5번 경우
elif all(numbers[i + 1] == numbers[i] + 1 for i in range(4)):
    print(max(numbers) + 500)
# 6번 경우
elif numbers.count(numbers[2]) == 3:
    print(numbers[2] + 400)
# 7번 경우
elif ((numbers[0] == numbers[1] and numbers[3] == numbers[4]) or
      (numbers[0] == numbers[1] and numbers[2] == numbers[3]) or
      (numbers[1] == numbers[2] and numbers[3] == numbers[4])):
    print(numbers[3] * 10 + numbers[1] + 300)
else:
    # 8번 경우
    found_two = False
    index = 0
    for i in range(4):
        if numbers[i] == numbers[i + 1]:
            found_two = True
            index = i
            break
    if found_two:
        print(numbers[index] + 200)

    # 9번 경우(아무것도 해당 안 됨)
    else:
        print(max(numbers) + 100)
