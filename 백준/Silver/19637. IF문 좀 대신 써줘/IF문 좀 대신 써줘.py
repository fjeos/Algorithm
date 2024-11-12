import sys
input = lambda: sys.stdin.readline().rstrip()

num_titles, num_characters = map(int, input().split())

titles = []
limits = set()
for _ in range(num_titles):
    title, limit = input().split()
    if limit not in limits:
        titles.append((title, int(limit)))
        limits.add(int(limit))

for _ in range(num_characters):
    power = int(input())
    start, end = 0, len(titles) - 1
    answer = ""
    while start <= end:
        mid = (start + end) // 2
        if power <= titles[mid][1]:
            answer = titles[mid][0]
            end = mid - 1
        elif power > titles[mid][1]:
            start = mid + 1

    print(answer)