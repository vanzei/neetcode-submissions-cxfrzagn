class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0
        l = r = 0
        hm = {}

        while r < len(s):
            hm[s[r]] = 1 + hm.get(s[r], 0)

            maxf = max(hm[s[r]], maxf)

            while ( r- l + 1 ) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

        