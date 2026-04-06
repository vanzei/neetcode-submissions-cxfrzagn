class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = dict()
        for i,num in enumerate(nums):
            if num in dif:
                return [dif[num], i]
            dif[target - num] = i

        