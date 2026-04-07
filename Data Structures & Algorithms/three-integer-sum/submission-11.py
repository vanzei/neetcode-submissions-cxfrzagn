class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                partial = nums[i] + nums[j] + nums[k]
                if partial == 0:
                    if [nums[i],nums[j], nums[k]] not in res:
                        res.append([nums[i],nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif partial > 0:
                    k -=1
                else:
                    j += 1
        print(res)
        return res

