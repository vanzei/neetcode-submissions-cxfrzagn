class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cA = Counter(s)
        cB = Counter(t)
        return cA == cB
        