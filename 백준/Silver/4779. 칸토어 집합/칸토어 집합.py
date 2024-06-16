import sys
input = lambda: sys.stdin.readline().rstrip()

def contour(num):
    if num == 0:
        return "-"
    else:
        return contour(num-1) + " "*len(contour(num-1)) + contour(num-1)


while(True):
    N = input()
    if len(N) == 0:
        break
    print(contour(int(N)))