class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                cur = 1
                while (num + cur) in set_nums:
                    cur += 1
                
                longest = max(longest, cur)
        return longest