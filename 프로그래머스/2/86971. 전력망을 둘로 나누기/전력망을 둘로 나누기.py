from collections import deque

def bfs(start, end, visited, graph):
    visited[start] = True
    visited[end] = True
    count = 1
    queue = deque()
    queue.append(end)
    
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                count += 1
                visited[next] = True
                
    return count


def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n + 1)]    
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    for start, end in wires:
        visited = [False] * (n + 1)
        count_tree1 = bfs(start, end, visited, graph)
        count_tree2 = abs(n - count_tree1)
        answer = min(answer, abs(count_tree1 - count_tree2))
    
    return answer
    