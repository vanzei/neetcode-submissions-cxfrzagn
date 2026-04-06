class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def count_sort():
            maxV, minV = max(nums), min(nums)
            count = defaultdict(int)

            for value in nums:
                count[value] += 1

            index =0
            for k in range(minV, maxV+1):
                while count[k] > 0:
                    nums[index] = k
                    index += 1
                    count[k] -= 1
            
        count_sort()
        return nums

        