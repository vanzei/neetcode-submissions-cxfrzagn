class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {}
        maxV, minV = max(nums), min(nums)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        i = 0
        for c in range(minV, maxV + 1):
            while c in counter and counter[c] > 0:
                nums[i] = c
                counter[c] -= 1
                i += 1