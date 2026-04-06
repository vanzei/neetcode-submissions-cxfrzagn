class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        for charS in s:
            if charS in hashMapS:
                hashMapS[charS] += 1
            else:
                hashMapS[charS] = 1
        for charT in t:
            if charT in hashMapT:
                hashMapT[charT] += 1
            else:
                hashMapT[charT] = 1
        
        return hashMapS == hashMapT