import math

xA, yA, xB, yB, xC, yC = map(int, input().split())
lengths = [math.sqrt(abs(xA - xB) ** 2 + abs(yA - yB) ** 2), math.sqrt(abs(xB - xC) ** 2 + abs(yB - yC) ** 2),
           math.sqrt(abs(xC - xA) ** 2 + abs(yC - yA) ** 2)]

if (xA - xB) * (yA - yC) == (xA - xC) * (yA - yB):
    print(-1.0)
else:
    print(2 * (max(lengths) - min(lengths)))
