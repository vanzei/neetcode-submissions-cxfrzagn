class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 
        n_nums = [-n for n in nums]
        heapq.heapify(n_nums)

        while k > 0:
            res = heapq.heappop(n_nums)
            k -= 1
        return -res