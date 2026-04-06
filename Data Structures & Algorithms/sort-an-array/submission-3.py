class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        mi, ma = min(nums), max(nums)
        for x in range(mi, ma + 1, 1):
            while x in c and c[x] != 0:
                res.append(x)
                c[x] -= 1
        print(res)
        return res
