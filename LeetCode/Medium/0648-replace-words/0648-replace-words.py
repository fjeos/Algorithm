class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()

        for j in range(len(words)):
            for i in range(len(words[j])):
                if words[j][:i+1] in dictionary:
                    words[j] = words[j][:i+1]
                    break
        return ' '.join(words)