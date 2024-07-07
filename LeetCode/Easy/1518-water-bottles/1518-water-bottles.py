class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while numBottles >= 1:
            drunk += empty // numExchange
            if empty % numExchange == 0:
                empty = 0
                numBottles //= numExchange
            else:
                numBottles = empty // numExchange
                empty %= numExchange
            empty += numBottles
        return drunk