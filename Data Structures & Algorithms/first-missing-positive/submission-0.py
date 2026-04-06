class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        check = [False] * n

        for num in nums:
            if num > 0 and num <= n:
                check[num-1] = True
        
        for num in range(1, n + 1):
            if not check[num - 1]:
                return num
        return n + 1