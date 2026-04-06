class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if (n - 1) not in numset:
                leng = 1
                while (n + leng) in numset:
                    leng += 1
                longest = max(longest, leng)
        return longest
        