def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    value = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = value
            value += 1
    for query in queries:
        min_value = 1e9
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        prev, x, y = matrix[x1][y1], x1, y1
        for y in range(y, y2+1):
            min_value = min(min_value, prev)
            temp = matrix[x][y]
            matrix[x][y] = prev
            prev = temp
        x += 1
        for x in range(x, x2+1):
            min_value = min(min_value, prev)
            temp = matrix[x][y]
            matrix[x][y] = prev
            prev = temp
        y -= 1
        for y in range(y, y1-1, -1):
            min_value = min(min_value, prev)
            temp = matrix[x][y]
            matrix[x][y] = prev
            prev = temp
        x -= 1
        for x in range(x, x1-1, -1):
            min_value = min(min_value, prev)
            temp = matrix[x][y]
            matrix[x][y] = prev
            prev = temp
        answer.append(min_value)

    return answer