def diff_check(a, b):
    diff = 0
    for a_1, b_1 in zip(a, b):
        if a_1 != b_1:
            diff += 1
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    length = len(words)
    visited = [False] * length
    result = 1e9
    def dfs(now, depth):
        nonlocal result
        if now == target:
            result = min(result, depth)
            return
        for i in range(length):
            if not visited[i] and diff_check(now, words[i]):
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False
            
    dfs(begin, 0)
    return result if result != 1e9 else 0