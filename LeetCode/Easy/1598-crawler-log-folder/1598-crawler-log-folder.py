class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = "main"
        path = [curr]
        
        for log in logs:
            if log == "../":
                if curr != "main":
                    curr = path[len(path)-2]
                    path.pop()
            elif log == "./":
                continue
            else:
                path.append(log)
                curr = log
                
        return len(path)-1