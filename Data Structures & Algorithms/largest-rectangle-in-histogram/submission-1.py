class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxV = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxV = max(maxV, height * (i - index))
                start = index
            stack.append([start, h])

        for i, h in stack:
            maxV = max(maxV, h * (len(heights) - i))
        return maxV