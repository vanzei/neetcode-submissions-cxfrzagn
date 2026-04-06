class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            lg = len(word)
            res += str(lg) + "#" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            lg = int(s[i:j])
            i = j + 1
            j = i + lg
            res.append(s[i:j])
            i = j
        return res
