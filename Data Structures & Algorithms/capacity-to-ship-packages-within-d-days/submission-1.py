class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def CanShip(cap):
            ship, curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    ship += 1
                    curCap = cap
                curCap -= w
            return ship <= days

        while l <= r :
            m = l + (r - l) // 2

            if CanShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res