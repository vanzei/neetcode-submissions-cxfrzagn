class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j :
            if not self.isAlpha(s[i]):
                i+= 1
                continue

            if not self.isAlpha(s[j]):
                j -= 1
                continue

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

    def isAlpha(self, string):
        if (ord(string) >= ord("a") and ord(string) <= ord("z"))\
        or (ord(string) >= ord("A") and ord(string) <= ord("Z"))\
        or (ord(string) >= ord("0") and ord(string) <= ord("9")):
            return True
    