class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mH= min(heights[r], heights[l]) * (r - l)
        while l < r:
            
            if heights[l] > heights[r]:
                r -=1
            else:
                l += 1
            print(r,l)
            mH = max(mH, min(heights[r], heights[l]) * (r - l))
    
        return mH

        