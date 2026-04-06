class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            cur = 0
            if num - 1 in nums:
                continue
            else:
                cur += 1
                while num + 1 in nums:
                    num += 1
                    cur += 1

                res = max(cur, res)
        return res
            