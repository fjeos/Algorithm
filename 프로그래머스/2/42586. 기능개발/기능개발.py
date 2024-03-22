def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    index = 0
    while not all(num >= 100 for num in progresses):
        count = 0
        while progresses[index] < 100:
            for i in range(N):
                if progresses[i] < 100:
                    progresses[i] += speeds[i]
        for j in range(index, N):
            if all(k >= 100 for k in progresses[index:j+1]):
                count += 1
            else:
                break
        answer.append(count)
        count = 0
        index = j                       
        
    return answer