class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        control = set()
        for j in range(len(s)):
            while s[j] in control:
                control.remove(s[i])
                i += 1
            control.add(s[j])
            res = max(res, j - i +1 )
        
        return res
                
            
