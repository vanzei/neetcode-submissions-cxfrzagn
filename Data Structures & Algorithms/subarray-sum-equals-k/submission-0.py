class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = {}
        res = 0
        prefSum[0] = 1
        cursum = 0
        for num in nums:
            cursum += num
            diff = cursum - k
            res += prefSum.get(diff, 0)
            prefSum[cursum] = 1 + prefSum.get(cursum, 0)
        return res

