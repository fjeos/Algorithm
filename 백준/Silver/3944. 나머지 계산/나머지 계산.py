import sys
input = lambda: sys.stdin.readline().rstrip()

for _  in range(int(input())):
    jin, su = input().split()
    print(sum(list(map(int, su))) % (int(jin) - 1))