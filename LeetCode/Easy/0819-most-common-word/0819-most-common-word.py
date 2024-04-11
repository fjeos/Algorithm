class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        
        words = []
        # ,과 공백으로 구분한 문자열 중 빈 문자열이 아닌 것만 words 리스트에 추가
        for word in re.split("[^a-z]", paragraph.lower()):
            if not word:
                continue
            words.append(word)
            
        # 각 단어를 count한 counter 생성
        counted = collections.Counter(words)

        # 금지된 단어가 있으면
        if banned:
            # counted 딕셔너리에서 해당 단어 삭제
            for ban in banned:
                del counted[ban]

        # 딕셔너리에서 최대 value를 가지는 key 값 리턴
        return max(counted, key = counted.get)