class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        
        if source == destination:
            return True
        
        for u, v in edges:
            graph[u] += [v]
            graph[v] += [u]
        
        queue = deque(graph[source])
        
        while queue:
            node = queue.popleft()
            for v in graph[node]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
            
        return True if visited[destination] else False
                
        
        