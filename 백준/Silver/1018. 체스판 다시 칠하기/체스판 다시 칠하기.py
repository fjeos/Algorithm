N, M = map(int, input().split())
board = []
result = []
for _ in range(N):
    board.append(input())
    
for i in range(N-7): 
    for j in range(M-7):
        countW = 0
        countB = 0
        for k in range(8):
            for l in range(8):
                if (k+l) % 2 == 0:
                    if board[i+k][j+l] != 'W':
                        countW += 1
                    if board[i+k][j+l] != 'B':
                        countB += 1
                else:
                    if board[i+k][j+l] != 'B':
                        countW += 1
                    if board[i+k][j+l] != 'W':
                        countB += 1
        result.append(countW)
        result.append(countB)      
        
print(min(result))               