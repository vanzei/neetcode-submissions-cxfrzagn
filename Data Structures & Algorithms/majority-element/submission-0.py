class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        print(counts)

        for c in counts:
            print(c)
            if counts[c] > len(nums)/2:
                return c

        