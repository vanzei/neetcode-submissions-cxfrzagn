class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for x, v in count.items():
            freq[v].append(x)

        res = []

        for val in range(len(freq) -1,0,-1):
            for n in freq[val]:
                res.append(n)
                if len(res) == k:
                    return res
