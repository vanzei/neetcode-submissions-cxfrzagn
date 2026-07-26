class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        i = 0
        res = []
        nums.sort()
        while i <= len(nums) - 3:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                S = nums[i] + nums[j] + nums[k]
                if S == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif S > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res
