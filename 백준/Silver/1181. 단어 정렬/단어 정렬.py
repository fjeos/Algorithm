words = [input() for _ in range(int(input()))]
words = list(set(words))
words.sort()
words.sort(key=len)
print('\n'.join(map(str, words)))