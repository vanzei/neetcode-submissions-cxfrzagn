class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            res.append(s[j+1: j+1+num])
            i = j+1+num
            j = i
        return res


