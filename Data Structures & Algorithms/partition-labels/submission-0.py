class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(s)):
            value = s[i]
            hashmap[value] = i

        clenght = 0
        end = 0
        i = 0
        while i < len(s):
            clenght += 1
            value = s[i]
            end = max(end, hashmap[value])

            if end == i:
                res.append(clenght)
                clenght = 0
            i += 1
        return res