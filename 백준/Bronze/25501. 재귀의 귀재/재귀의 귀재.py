import sys
input = lambda: sys.stdin.readline().rstrip()

def recursion(s, l, r, count):
    count += 1
    if l >= r: return [1, count]
    elif s[l] != s[r]: return [0, count]
    else: return recursion(s, l+1, r-1, count)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

for _ in range(int(input())):
    result = 0
    print(' '.join(map(str, isPalindrome(input(), result))))