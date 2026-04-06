class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l in range(len(s)) and not self.isAlp(s[l]):
                l += 1
            while r in range(len(s)) and not self.isAlp(s[r]):
                r -= 1
            while l in range(len(s)) and r in range(len(s)) and self.isAlp(s[l]) and self.isAlp(s[r]):
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
        return True
                 
        

    
    def isAlp(self, value):
        if ord('a') <= ord(value) <= ord('z') or ord('A') <= ord(value) <= ord('Z') or ord('0') <= ord(str(value)) <= ord('9'):
            return True