class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        
        #리스트에 0보다 큰 값이 있는 동안 반복
        while any(0 < num for num in tickets):
            for i in range(len(tickets)):
                
                #티켓 구매가 끝났으면 무시
                if tickets[i] == 0:
                    continue
                #티켓을 하나 구매하고, 횟수를 1 증가
                tickets[i] -= 1
                answer += 1
                #k번째 사람의 티켓 구매가 끝났으면 종료
                if tickets[k] == 0:
                    return answer