import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = [input() for _ in range(N)]
answer = ''


def check_white(arr):
    is_white = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != '0':
                is_white = False
                break
        if not is_white:
            break
    if is_white:
        return True


def check_black(arr):
    is_black = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != '1':
                is_black = False
                break
        if not is_black:
            break
    if is_black:
        return True


def recur(arr):
    global answer
    if arr[0][0] == '0':
        if check_white(arr):
            answer += '0'
            return
    else:
        if check_black(arr):
            answer += '1'
            return

    answer += '('
    temp = []
    for k in range(len(arr) // 2):
        temp.append(arr[k][:len(arr) // 2])
    recur(temp)
    temp = []
    for k in range(len(arr) // 2):
        temp.append(arr[k][len(arr) // 2:])
    recur(temp)
    temp = []
    for k in range(len(arr) // 2, len(arr)):
        temp.append(arr[k][:len(arr) // 2])
    recur(temp)
    temp = []
    for k in range(len(arr) // 2, len(arr)):
        temp.append(arr[k][len(arr) // 2:])
    recur(temp)
    answer += ')'


if tree[0][0] == '0':
    if check_white(tree):
        print(0)
        exit(0)
else:
    if check_black(tree):
        print(1)
        exit(0)

temp = []
for k in range(N // 2):
    temp.append(tree[k][:N // 2])
recur(temp)
temp = []
for k in range(N // 2):
    temp.append(tree[k][N // 2:])
recur(temp)
temp = []
for k in range(N // 2, N):
    temp.append(tree[k][:N // 2])
recur(temp)
temp = []
for k in range(N // 2, N):
    temp.append(tree[k][N // 2:])
recur(temp)
print(f"({answer})")
