class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        partial = []
        def backtracking(i):
            if i >= len(nums):
                res.append(partial.copy())
                return
            #print(partial)

            partial.append(nums[i])
            backtracking(i + 1)
            partial.pop()
            backtracking(i+1)
            

        backtracking(0)
        return res
            

                
        