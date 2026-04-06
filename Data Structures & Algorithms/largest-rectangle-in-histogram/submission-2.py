class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []

        for i, cur in enumerate(heights):
            start = i
            while stack and stack[-1][1] > cur:
                index, height = stack.pop()
                maxA = max(maxA, height *(i-index))
                start = index
            stack.append((start, cur))

        for i,h in stack:
            maxA = max(maxA, h * (len(heights)- i))
        
        return maxA
