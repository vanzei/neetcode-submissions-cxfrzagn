class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for i, v in count.items():
            freq[v].append(i)
        
        res = []
        for val in range(len(freq)-1,0,-1):
            for n in freq[val]:
                res.append(n)
                if len(res) == k:
                    return res
        