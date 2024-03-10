from itertools import combinations
while True:
    lists = list(map(int, input().split()))
    k = lists[0]
    if k == 0: break
    lotto = list(combinations(lists[1:], 6))
    for i in lotto:
        print(' '.join(map(str, i)))
    print()