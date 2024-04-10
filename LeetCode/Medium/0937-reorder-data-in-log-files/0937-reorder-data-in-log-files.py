class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        #각 log가 숫자이면 digits 리스트에, 문자이면 letters 리스트에 추가
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        #letters 리스트를 식별자를 제외한 값으로 정렬하고, 모두 같으면 식별자를 기준으로 정렬
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        #letter 리스트와 digits 리스트를 연결하여 리턴
        return letters + digits