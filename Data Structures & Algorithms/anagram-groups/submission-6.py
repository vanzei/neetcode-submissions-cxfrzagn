class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sS = "".join(sorted(s))
            if sS in anagrams:
                anagrams[sS].append(s)
            else:
                anagrams[sS] = [s]
        res = []
        for value in anagrams.values():
            res.append(value)
        return res