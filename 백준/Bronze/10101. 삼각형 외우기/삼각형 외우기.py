import sys
input = lambda: sys.stdin.readline().rstrip()
lists = [int(input()) for _ in range(3)]
print("Error" if sum(lists) != 180 else ["Equilateral", "Isosceles", "Scalene"][len(set(lists))-1])