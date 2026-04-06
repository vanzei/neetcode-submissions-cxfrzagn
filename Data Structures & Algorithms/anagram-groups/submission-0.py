class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = dict()
        for word in strs:
            if ''.join(sorted(word)) in sets:
                sets[''.join(sorted(word))].append(word)
            else:
                sets[''.join(sorted(word))] = [word]
        res = []
        for items in sets:
            res.append(sets[items])
        return res
        