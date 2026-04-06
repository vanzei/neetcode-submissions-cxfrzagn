class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        i = 0
        while i < len(nums) -2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                print([nums[i], nums[j], nums[k]])
                if nums[i] + nums[j] + nums[k] == 0:
                    if ([nums[i], nums[j], nums[k]]) not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k in range(len(nums)) and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res
            
        

        