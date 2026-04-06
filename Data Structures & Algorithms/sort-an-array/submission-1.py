class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            count = defaultdict(int)
            maxV, minV = max(nums), min(nums)

            for v in nums:
                count[v] += 1

            index = 0
            for value in range(minV, maxV + 1):
                while count[value] > 0 :
                    nums[index] = value
                    index += 1
                    count[value] -= 1

        counting_sort()
        return nums

        