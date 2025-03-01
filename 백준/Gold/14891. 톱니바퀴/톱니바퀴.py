import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

one = deque(input())
two = deque(input())
three = deque(input())
four = deque(input())

for _ in range(int(input())):
    tobni, direction = map(int, input().split())
    if tobni == 1:
        if one[2] != two[6]:
            if two[2] != three[6]:
                if three[2] != four[6]:
                    four.rotate(-direction)
                three.rotate(direction)
            two.rotate(-direction)
        one.rotate(direction)
    elif tobni == 2:
        if two[6] != one[2]:
            one.rotate(-direction)
        if two[2] != three[6]:
            if three[2] != four[6]:
                four.rotate(direction)
            three.rotate(-direction)
        two.rotate(direction)
    elif tobni == 3:
        if three[6] != two[2]:
            if two[6] != one[2]:
                one.rotate(direction)
            two.rotate(-direction)
        if three[2] != four[6]:
            four.rotate(-direction)
        three.rotate(direction)
    else:
        if four[6] != three[2]:
            if three[6] != two[2]:
                if two[6] != one[2]:
                    one.rotate(-direction)
                two.rotate(direction)
            three.rotate(-direction)
        four.rotate(direction)
answer = 0
if one[0] == '1':
    answer += 1
if two[0] == '1':
    answer += 2
if three[0] == '1':
    answer += 4
if four[0] == '1':
    answer += 8
print(answer)