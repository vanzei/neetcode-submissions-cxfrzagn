class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for n in numset:
            if (n - 1) not in numset:
                leng = 1
                while (n + leng) in numset:
                    leng += 1
                longest = max(leng, longest)
        return longest
        