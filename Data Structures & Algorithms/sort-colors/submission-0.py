class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def count_sort():
            count = defaultdict(int)
            for num in nums:
                count[num] += 1
            index = 0
            for x in range(0, 3):
                while count[x] > 0:
                    
                    nums[index] = x
                    index += 1
                    count[x] -= 1
                    
                    
        
        count_sort()
        return nums
            
        