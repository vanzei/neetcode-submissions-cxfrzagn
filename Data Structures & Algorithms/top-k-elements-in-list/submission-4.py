class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freq = {}
        for num, q in counter.items():
            if q in freq:
                freq[q].append(num)
            else:
                freq[q] = [num]
        
        res = []

        for x in range(len(nums), 0, -1):
            if x in freq:
                for y in freq[x]:
                    res.append(y)
                    if len(res) == k:
                        return res
