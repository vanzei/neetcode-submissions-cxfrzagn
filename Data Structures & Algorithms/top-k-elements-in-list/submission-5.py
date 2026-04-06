class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        di = dict()
        for num in nums:
            if num in di:
                di[num] += 1
            else:
                di[num] = 1
        c = dict()
        for each in di:
            if di[each] in c:
                c[di[each]].append(each)
            else:
                c[di[each]] = [each]
        
        maxQ = len(nums)
        print(c)

        for x in range(maxQ, 0, -1):
            if x in c:
                for y in c[x]:
                    res.append(y)
                    if len(res) == k:
                        return res
