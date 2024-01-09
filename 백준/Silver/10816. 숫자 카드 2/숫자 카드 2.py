from collections import Counter
N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

count = Counter(card1)
for i in range(len(card2)):
    if card2[i] in count:
        print(count[card2[i]], end=' ')
    else:
        print(0, end=' ') 