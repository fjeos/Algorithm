from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
numbers = [int(input()) for _ in range(N)]

counter = Counter(numbers)
cnt = counter.most_common()
freq = []

print(round(sum(numbers)/N))
print(sorted(numbers)[N//2])
maximum = cnt[0][1]
for num in cnt:
    if num[1] == maximum:
        freq.append(num[0])
if len(freq) < 2:
    print(freq[0])
else:
    print(sorted(freq)[1])
print(max(numbers) - min(numbers))