def solution(board, moves):
    answer = 0
    N = len(board)
    basket = []
    for i in range(len(moves)):
        index = 0
        while board[index][moves[i]-1] == 0 and index < N-1: 
            index += 1
        if board[index][moves[i]-1] != 0:
            basket.append(board[index][moves[i]-1])
            board[index][moves[i]-1] = 0
            if len(basket) > 1 and basket[-1] == basket[-2]:
                answer += 2
                basket.pop()
                basket.pop()
    return answer