class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1


        maxV = min(heights[i], heights[j]) * ( j - i )
        while i < j:
            cur = min(heights[i], heights[j]) * ( j - i)
            maxV = max(maxV, cur)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        return maxV
        