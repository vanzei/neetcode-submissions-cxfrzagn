class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter = {}
        maxV, minV = max(nums), min(nums)
        res = []
        for num in nums:
            c = counter.get(num,0) + 1
            counter[num] = c
        for x in range(minV, maxV+1):
            while x in counter and counter[x] > 0:
                res.append(x)
                counter[x] -= 1
        return res
