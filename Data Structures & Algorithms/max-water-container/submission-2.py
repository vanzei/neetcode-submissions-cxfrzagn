class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxC = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cArea = min(heights[l], heights[r]) * (r - l)
            maxC = max(maxC, cArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxC

        