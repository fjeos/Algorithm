class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        table = {}

        for i in range(len(words[0])):
            table[words[0][i]] = words[0].count(words[0][i])
            for j in range(1, len(words)):
                cmp = words[j].count(words[0][i])
                table[words[0][i]] = min(table[words[0][i]], cmp)

        for key, value in table.items():
            for k in range(value):
                result.append(key)

        return result
        