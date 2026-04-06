class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxL = 1
        l = 0
        un = set()
        for r in range(len(s)):
            while s[r] in un:
                un.remove(s[l])
                l += 1
            un.add(s[r])
            maxL = max(maxL, r -l + 1)
        return maxL
                

