class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = [i+1 for i in range(n)]
        index = 0
        while len(friends) > 1:
            count = 1
            while count < k:
                if index >= len(friends):
                    index = 0
                index += 1
                count += 1
            if index >= len(friends):
                index = 0
            friends.pop(index)
        return friends[0]