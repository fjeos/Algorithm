import heapq
def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    heap = []
    
    for i, en in enumerate(enemy):
        heapq.heappush(heap, -en)
        n -= en
        if n < 0:
            if k > 0:
                k -= 1
                n += -heapq.heappop(heap)
            else:
                return i
                
    return len(enemy)