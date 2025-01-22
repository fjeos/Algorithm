def solution(k, ranges):
    answer = []
    tuples = [(0, k)]
    i = 1
    while k != 1:
        if k % 2 == 0:
            tuples.append((i, k // 2))
            k //= 2
        else:
            tuples.append((i, k * 3 + 1))
            k = k * 3 + 1
        i += 1
    
    for a, b in ranges:
        if b <= 0:
            b = len(tuples) - 1 + b
            if a > b:
                answer.append(-1.0)
                continue
        area = 0
        for i in range(a, b):
            m = (tuples[i][1] - tuples[i+1][1]) / (tuples[i][0] - tuples[i+1][0])
            c = tuples[i][1] - m * tuples[i][0]
            
            x1, x2 = tuples[i][0], tuples[i+1][0]
            area += (m / 2) * (x2**2 - x1**2) + c * (x2 - x1)
        answer.append(float(area))
            
            
    return answer