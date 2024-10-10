def star(num):
    if num == 1:
        return ['*']
    stars = star(num // 3)
    result = []
    for i in stars:
        result.append(i * 3)
    for j in stars:
        result.append(j + ' ' * (num//3) + j)
    for k in stars:
        result.append(k * 3)

    return result


print("\n".join(star(int(input()))))
