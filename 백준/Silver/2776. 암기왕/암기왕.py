from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    note1 = defaultdict(int)
    int(input())
    nums = list(input().split())
    for num in nums:
        note1[num] = 1
    int(input())
    note2 = list(input().split())
    for num in note2:
        print(1 if note1[num] == 1 else 0)