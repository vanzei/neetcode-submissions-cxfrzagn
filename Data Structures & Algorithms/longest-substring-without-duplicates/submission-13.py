class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest  = 1

        i, j = 0, 0
        cur = []
        while j < len(s):
            if s[j] not in cur:
                cur.append(s[j])
                longest = max(len(cur), longest)
                j += 1
            else:
                while s[j] in cur:
                    cur.remove(s[i])
                    i += 1
        return longest
                
                    