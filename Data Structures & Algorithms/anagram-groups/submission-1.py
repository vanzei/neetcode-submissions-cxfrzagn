class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = dict()
        for word in strs:
            if ''.join(sorted(word)) in sets:
                sets[''.join(sorted(word))].append(word)
            else:
                sets[''.join(sorted(word))] = [word]
        return list(sets.values())
        