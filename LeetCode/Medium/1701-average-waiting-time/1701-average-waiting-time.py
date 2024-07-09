class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = [customers[0][1]]
        
        # 끝난 시간
        end_time = customers[0][0] + customers[0][1]
        
        customers.pop(0)
        
        for arrival, time in customers:
            if end_time < arrival:
                end_time = arrival + time
                waiting.append(time)
                continue
            # 끝난 시간 계산
            end_time += time
            waiting.append(end_time - arrival)
            
        return sum(waiting) / (len(customers) + 1)