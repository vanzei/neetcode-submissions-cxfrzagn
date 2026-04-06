class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:

            if (num - 1) not in set_nums:
                curL = 1
                while (num + curL) in set_nums:
                    curL += 1
                
                longest = max(longest, curL)
        return longest

        
        
                

        