class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import defaultdict
        hand.sort()
        freq = defaultdict(int)
        for x in hand:
            freq[x] += 1

        if len(hand) % groupSize == 0:
            for curr in hand:
                if freq[curr] < 1:
                    continue
                possible = True
                for x in range(curr, curr + groupSize):
                    if freq[x] > 0:
                        freq[x] -= 1
                    else:
                        possible = False
                if not possible:
                    return False

            return True

        else:
            return False