N = int(input())
target = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num = 2
x, y = N // 2, N // 2
arr[x][y] = 1
position = [x+1, y+1]
repeat = 0
while True:
    for i in range(4):
        for _ in range(repeat):
            x += dx[i]
            y += dy[i]
            arr[x][y] = num
            if num == target:
                position = [x+1, y+1]
            num += 1
    if x == y == 0:
        break
    x -= 1
    y -= 1
    repeat += 2
    
for nums in arr:
    print(' '.join(map(str, nums)))
print(position[0], position[1])
