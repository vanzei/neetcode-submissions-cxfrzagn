class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + ( r - l) // 2
            cur = 0
            for pile in piles:
                cur += math.ceil(float(pile)/m)
            if cur <= h:
                res = m
                r = m -1
            else:
                l = m +1
        return res

