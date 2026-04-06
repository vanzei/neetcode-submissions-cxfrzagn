class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        post = 1
        print(res)
        for j in range(len(nums)-1, -1, -1):
            res[j] *= post 
            post *= nums[j]

        return res
