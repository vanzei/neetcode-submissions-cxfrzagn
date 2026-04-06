class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for i in hand:
            count[i]  = 1 + count.get(i, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for x in range(first, first + groupSize):
                if x not in count:
                    return False
                count[x] -= 1
                if count[x] == 0:
                    if x != minH[0]:
                        return False

                    heapq.heappop(minH)
        return True

        