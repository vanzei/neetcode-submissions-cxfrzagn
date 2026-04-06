class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_h = dict()
        for index, val in enumerate(nums):
            diff = target - val
            if diff in diff_h:
                return [diff_h[diff], index]
            diff_h[val] = index
        

        