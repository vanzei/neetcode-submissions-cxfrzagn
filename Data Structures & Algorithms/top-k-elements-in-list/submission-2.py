class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums)+ 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for c, v in count.items():
            freq[v].append(c)

        res = []
        for x in range(len(freq) - 1, 0, -1):
            for n in freq[x]:
                res.append(n)
                if len(res) == k:
                    return res