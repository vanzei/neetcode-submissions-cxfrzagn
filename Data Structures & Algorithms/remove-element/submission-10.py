class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                j -=1
                nums[i] = nums[j]
                
            else:
                i+= 1
        
        return j

        