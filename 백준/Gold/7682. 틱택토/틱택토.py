import sys

input = lambda: sys.stdin.readline().rstrip()
board = []
while True:
    line = input()
    if line == "end":
        break
    board.append(list(list(line[i:i + 3]) for i in range(0, 9, 3)))

for row in board:
    count_X, count_O = 0, 0
    has_blank = False
    for el in row:
        if '.' in el:
            has_blank = True
        count_X += el.count('X')
        count_O += el.count('O')
    if abs(count_X - count_O) > 1:
        print("invalid")
    else:
        result = ""
        is_O, is_X = False, False
        # 가로 ,세로, 대각선 - X
        if row[0][0] == row[0][1] == row[0][2] == 'X' or \
                row[1][0] == row[1][1] == row[1][2] == 'X' or \
                row[2][0] == row[2][1] == row[2][2] == 'X' or \
                row[0][0] == row[1][1] == row[2][2] == 'X' or \
                row[0][2] == row[1][1] == row[2][0] == 'X' or \
                row[0][0] == row[1][0] == row[2][0] == 'X' or \
                row[0][1] == row[1][1] == row[2][1] == 'X' or \
                row[0][2] == row[1][2] == row[2][2] == 'X':
            is_X = True
        if row[0][0] == row[0][1] == row[0][2] == 'O' or \
                row[1][0] == row[1][1] == row[1][2] == 'O' or \
                row[2][0] == row[2][1] == row[2][2] == 'O' or \
                row[0][0] == row[1][1] == row[2][2] == 'O' or \
                row[0][2] == row[1][1] == row[2][0] == 'O' or \
                row[0][0] == row[1][0] == row[2][0] == 'O' or \
                row[0][1] == row[1][1] == row[2][1] == 'O' or \
                row[0][2] == row[1][2] == row[2][2] == 'O':
            is_O = True
        if is_X and is_O:
            result = "invalid"
        elif is_X:
            result = "valid" if count_X != count_O else "invalid"
        elif is_O:
            result = "valid" if count_X == count_O else "invalid"
        else:
            result = "valid" if not has_blank and count_X - count_O == 1 else "invalid"
        print(result)

