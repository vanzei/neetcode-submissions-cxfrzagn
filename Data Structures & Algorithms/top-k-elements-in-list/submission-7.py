class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freqc = [[] for i in range(len(nums) + 1)]
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for n, v in counter.items():
            freqc[v].append(n)
        
        res = []
        for i in range(len(freqc) - 1, 0, -1):
            for num in freqc[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
        