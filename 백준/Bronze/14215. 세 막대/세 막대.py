lists = list(map(int, input().split()))
lists.sort()
while lists[0] + lists[1] <= lists[2]:
    lists[2] -= 1
print(sum(lists))
