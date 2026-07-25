class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        for x, v in enumerate(s):
            j = i + 1
            while j < len(s) and s[j] != "#":
                j += 1
            if i >= len(s):
                return res
            lString = int(s[i:j])
            res.append(s[j+1: j+1+lString])
            i = j+1+lString
        return res
