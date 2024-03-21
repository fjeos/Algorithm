# def solution(sequence, k):
#     answer = []
#     N = len(sequence)
#     summation = 0
#     end = 0
    
#     for i in range(N):
#         while summation < k and end < N:
#             summation += sequence[end]
#             end += 1
            
#         if summation == k:
#             answer.append([i, end-1, end-1-i])
            
#         summation -= sequence[i]
#         answer.sort(key = lambda x: x[2])
#     return answer[0][:2]

def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):

        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    return res[0][:2]