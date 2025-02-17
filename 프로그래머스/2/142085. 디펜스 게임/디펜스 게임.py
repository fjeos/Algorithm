import heapq
def solution(n, k, enemy):
    length = len(enemy)
    if length <= k or sum(enemy) <= n:
        return length
    heap = []
    for i in range(length):
        n -= enemy[i]
        heapq.heappush(heap, (-enemy[i], enemy[i]))
        if n < 0:
            if k > 0:
                if heap:
                    k -= 1
                    n += heapq.heappop(heap)[1]
                else:
                    k -= 1
            else:
                if n >= enemy[i]:
                    n -= enemy[i]
                    heapq.heappush(heap, (-enemy[i], enemy[i]))
                else:
                    return i   
    return i + 1