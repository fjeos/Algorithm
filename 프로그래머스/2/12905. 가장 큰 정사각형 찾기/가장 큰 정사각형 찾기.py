from collections import deque
def solution(board):    
    dp = board[:]
    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y-1][x-1], dp[y][x-1], dp[y-1][x]) + 1
        
    return max(map(max, dp)) ** 2