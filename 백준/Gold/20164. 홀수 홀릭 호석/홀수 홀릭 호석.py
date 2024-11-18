def recur(num: str, count: int) -> list:
    max_value, min_value = 0, 1e9

    for i in num:
        if int(i) % 2 != 0:
            count += 1

    if len(num) == 1:
        return [count, count]
    elif len(num) == 2:
        return recur(str(int(num[0]) + int(num[1])), count)
    else:
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                result = recur(str(int(num[:i + 1]) + int(num[i + 1: j + 1]) + int(num[j + 1:])), count)
                min_value = min(min_value, result[0])
                max_value = max(max_value, result[1])

        return [min_value, max_value]


N = input()
answer = recur(N, 0)
print(f"{answer[0]} {answer[1]}")
