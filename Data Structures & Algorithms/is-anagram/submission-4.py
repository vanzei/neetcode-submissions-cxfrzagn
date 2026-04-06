class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_S= Counter(s)
        c_T  = Counter(t)
        return c_T == c_S