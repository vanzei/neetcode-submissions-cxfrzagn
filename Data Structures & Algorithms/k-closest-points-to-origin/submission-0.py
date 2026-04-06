class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            d = (p[0] ** 2 + p[1] ** 2) ** 0.5
            distances.append([d, p[0], p[1]])

        heapq.heapify(distances)
        res = []
        while k > 0:
            cur = heapq.heappop(distances)
            res.append([cur[1], cur[2]])
            k -= 1
        return res
