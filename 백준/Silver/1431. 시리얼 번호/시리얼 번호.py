import sys

def summ(number):
    summation = 0
    for i in number:
        if i.isdigit():
            summation += int(i)
    return summation

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = [chr(48+i) for i in range(10)]
serial = [input() for _ in range(N)]
serial.sort(key = lambda x:(len(x), summ(x), x))
print('\n'.join(serial))