class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        exist = dict()
        for i, st in enumerate(strs):
            st = "".join(sorted(st))
            if st in exist:
                exist[st].append(strs[i])
            else:
                exist[st] = [strs[i]]
        res = []
        for values in exist.values():
            res.append(values)
        return res

