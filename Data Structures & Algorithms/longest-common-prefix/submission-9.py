class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        res= ""

        for l in range(len(ref)):
            for s in strs:
                if l in range(len(s)) and ref[l] == s[l]:
                    continue
                else:
                    return res
            res += s[l]
        return res
            
        
        