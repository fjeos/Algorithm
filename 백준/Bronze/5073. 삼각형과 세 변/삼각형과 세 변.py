import sys
input = lambda: sys.stdin.readline().rstrip()
while True:
    lists = list(map(int, input().split()))
    if all(x == 0 for x in lists):
        break
    lists.sort()
    print("Invalid" if lists[0] + lists[1] <= lists[2] else ["Equilateral", "Isosceles", "Scalene"][len(set(lists))-1])