def check_success(diffs, times, limit, mid):
    total_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= mid:
            total_time += times[i]
        else:
            total_time += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i]

    return total_time <= limit

    
def solution(diffs, times, limit):
    start, end = min(diffs), max(diffs)
    if diffs[0] > (start + end) // 2:
        return 1
    answer = end
    while start <= end:
        mid = (start + end) // 2
        if check_success(diffs, times, limit, mid):
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
            
    return answer