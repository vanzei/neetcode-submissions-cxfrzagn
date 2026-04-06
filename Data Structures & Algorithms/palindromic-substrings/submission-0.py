class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for n in range(len(s)):

            l = r = n
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l = n
            r = n + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res       