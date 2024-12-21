import sys

input = lambda: sys.stdin.readline().rstrip()
alphabet = {chr(value): value for value in range(65, 91)}


def solve(word):
    result = []
    index = len(word) - 2
    while True:
        if alphabet[word[index]] < alphabet[word[index + 1]]:
            break
        index -= 1
    start_value = alphabet[word[index]]
    result.append(''.join(word[:index]))
    del word[:index]
    if len(word) > 1:
        min_value, max_value = alphabet[word[1]], alphabet[word[1]]
        index = 1
        for i in range(len(word)):
            if min_value > alphabet[word[i]] > start_value:
                min_value = alphabet[word[i]]
                index = i
            elif max_value < alphabet[word[i]]:
                max_value = alphabet[word[i]]
                index = i
        result.append(word[index])
        del word[index]
    result.append(''.join(sorted(word)))
    print(''.join(result))


for _ in range(int(input())):
    solve(list(input()))
