from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
line = list(map(int, input().split()))
stack = deque()
number = 1

for student in line:
    stack.append(student)
    
    while stack and stack[-1] == number:
        stack.pop()
        number += 1
        
print("Nice" if not stack else "Sad")