class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ""
        while i < len(strs[0]):
            for string in strs:
                if i < len(string) and strs[0][i] == string[i]:
                    continue
                else:
                    return res

                          
            res = res + string[i]
            i += 1
        return res
                

        