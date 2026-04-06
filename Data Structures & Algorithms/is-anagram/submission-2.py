class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_1= dict()
        c_2 = dict()
        for char in s:
            c_1[char] = c_1.get(char, 0) + 1
        
        for char in t:
            c_2[char] = c_2.get(char,0) + 1

        return c_1 == c_2
