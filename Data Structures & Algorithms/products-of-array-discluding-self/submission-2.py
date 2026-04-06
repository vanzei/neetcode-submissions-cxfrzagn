class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        l = 1
        for x in range(n):
            res[x] = l
            l *= nums[x]
        r = 1
        for x in range(n -1, -1, -1):
            res[x] *= r
            r *= nums[x]
        
        print(res)
        return res

