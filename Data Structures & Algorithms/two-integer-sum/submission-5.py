class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_diff = dict()
        for i,n in enumerate(nums):
            diff = target - n
            
            if n in set_diff:
                return [set_diff[n], i]
            set_diff[diff] = i