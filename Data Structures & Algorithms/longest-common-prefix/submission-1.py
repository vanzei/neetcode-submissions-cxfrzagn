class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ""

        while i < len(strs[0]):
            
            for word in strs:
                if i < len(word) and strs[0][i] == word[i]:
                    continue
                else:
                    return res
            res += strs[0][i]
            i += 1
            
        return res
        