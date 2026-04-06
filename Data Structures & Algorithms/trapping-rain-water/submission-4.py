class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i, j = 0, len(height) - 1
        maxL, maxR = height[i], height[j]
        res = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
                maxL = max(maxL, height[i])
                res += maxL - height[i]
            else:
                j -= 1
                maxR = max(maxR, height[j])
                res += maxR - height[j]
        return res
