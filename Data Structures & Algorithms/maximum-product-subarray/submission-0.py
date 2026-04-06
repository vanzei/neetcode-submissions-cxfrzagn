class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        cMax, cMin = 1, 1

        for num in nums:
            if num == 0:
                cMax, cMin = 1, 1
                continue
            temp = cMax * num
            cMax = max( num * cMax, num * cMin, num)
            cMin = min( num * cMin, temp, num)
            res = max(res, cMax, cMin)
        return res