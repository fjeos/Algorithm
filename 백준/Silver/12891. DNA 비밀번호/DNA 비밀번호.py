import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

tot_length, pw_length = map(int, input().split())
temp_DNA = input()
A, C, G, T = map(int, input().split())
now_pw = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
answer = 0

start, end = 0, pw_length - 1
queue = deque(temp_DNA[start:end])
for num in queue:
    now_pw[num] += 1
while end < tot_length:
    now_pw[temp_DNA[end]] += 1
    if now_pw['A'] >= A and now_pw['C'] >= C and now_pw['G'] >= G and now_pw['T'] >= T:
        answer += 1
    now_pw[temp_DNA[start]] -= 1
    start += 1
    end += 1

print(answer)
