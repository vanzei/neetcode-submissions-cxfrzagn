class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        control = len(strs[0])
        for i in range(0, control + 1):
            for word in strs:
                if i not in range(len(word)) or strs[0][i] != word[i]:
                    return res 
            res = res + strs[0][i]

        