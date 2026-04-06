class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        setnums = set(nums)
        for num in setnums:
            c = 1
            while num - 1 in setnums:
                c +=1
                longest = max(longest, c)
                num -=1

        return longest