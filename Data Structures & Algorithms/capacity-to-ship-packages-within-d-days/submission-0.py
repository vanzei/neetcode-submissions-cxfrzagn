class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        
        def canShip(cap):
            ships, cur = 1 , cap
            for w in weights:
                if cur - w < 0:
                    ships += 1
                    cur = cap
                cur -= w
            return ships <= days
        
        while l <= r:
            m = l  + (r - l) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

        
