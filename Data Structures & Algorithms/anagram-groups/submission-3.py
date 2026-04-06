class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []
        for strn in strs:
            key = "".join(sorted(strn))

            if key in groups:
                groups[key].append(strn)
            else:
                groups[key] = [strn]

        for k in groups:
            res.append(groups[k])
        print(res)
        return res
        