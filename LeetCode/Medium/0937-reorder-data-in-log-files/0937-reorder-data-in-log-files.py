class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        new_lists = []
        i = 0
        while i < len(logs):
            if logs[i][logs[i].index(' ')+1].isalpha():
                new_lists.append(logs[i].split())
                logs.pop(i)
                i -= 1
            i += 1
        new_lists.sort(key = lambda x: (x[1:], x[0]))
        for i in range(len(new_lists)):
            new_lists[i] = ' '.join(new_lists[i])
        new_lists.extend(logs)

        return new_lists