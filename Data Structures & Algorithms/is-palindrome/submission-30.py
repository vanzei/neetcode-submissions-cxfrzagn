class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            print(self.isalpha(s[i]),self.isalpha(s[j]))
            while i < len(s) and not self.isalpha(s[i]):
                i += 1
            while j >= 0 and not self.isalpha(s[j]):
                j -= 1
            if i in range(len(s)) and s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
            
        
        return True


        

    def isalpha(self, s):
        print(s)
        if (ord(s) >= ord("a") and ord(s) <= ord("z")) or (ord(s) >= ord("A") \
        and ord(s) <= ord("Z")) or \
        ( ord("0") <= ord(s) <=ord("9") ):
            return True