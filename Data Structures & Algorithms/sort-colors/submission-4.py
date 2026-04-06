class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        i = 0
        for x in range(0,3,1):
            while c[x] > 0:
                nums[i] = x
                c[x] -= 1
                i += 1
        print(nums)

            