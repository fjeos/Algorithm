import sys
input = lambda: sys.stdin.readline().rstrip()

N, new_score, P = map(int, input().split())
if N:
    scores = list(map(int, input().split()))
    scores.append(new_score)
    scores.sort(reverse=True)
    index = scores.index(new_score) + 1
    if index > P:
        print(-1)
    else:
        if N == P and new_score == scores[-1]:
            print(-1)
        else:
            print(index)
else:
    print(1)
