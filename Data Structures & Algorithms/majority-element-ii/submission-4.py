class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        reference = len(nums) / 3
        counter = {}
        freq = {}
        res = []
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        for i, v in counter.items():
            if v in freq:
                freq[v].append(i)
            else:
                freq[v] = [i]


        for x in range(len(nums),-1,-1):
            if x in freq and x > reference:
                for n in freq[x]:
                    res.append(n)
        
        return res