import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
people = [list(input().split()) for _ in range(N)]
rainbow = {'ChongChong'}
for i in range(N):
    if people[i][0] in rainbow or people[i][1] in rainbow:
        rainbow.add(people[i][0])
        rainbow.add(people[i][1])

print(len(rainbow))
