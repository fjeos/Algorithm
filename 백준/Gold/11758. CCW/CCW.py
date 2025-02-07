import sys

input = lambda: sys.stdin.readline().rstrip()

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

p12_x, p12_y = (x2 - x1), (y2 - y1)
p23_x, p23_y = (x3 - x2), (y3 - y2)

result = (p12_x * p23_y) - (p23_x * p12_y)

print(1 if result > 0 else -1 if result < 0 else 0)
