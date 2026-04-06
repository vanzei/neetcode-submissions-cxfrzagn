class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, partial, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(partial.copy())
                return
            
            partial.append(nums[i])
            backtrack(i, partial, total + nums[i])
            partial.pop()
            backtrack(i+1, partial, total)
        backtrack(0, [], 0)
        return res
