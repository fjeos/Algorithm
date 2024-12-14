import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = list(set(input() for _ in range(N)))
answer = 0
for a_word in words:
    is_prefix = True
    for b_word in words:
        if a_word == b_word:
            continue
        if a_word in b_word[:len(a_word)]:
            is_prefix = False
            break
    if is_prefix:
        answer += 1

print(answer)