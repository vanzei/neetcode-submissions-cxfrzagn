class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0

        i, j = 0, len(heights) - 1

        while i < j:
            current = (j - i) * min(heights[j], heights[i])
            largest = max(current, largest)
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        return largest
            