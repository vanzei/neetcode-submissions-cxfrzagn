class Solution:
    def validPalindrome(self, s: str) -> bool:        
        def pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0 , len(s)-1

        while l < r:
            print(l,r)
            if s[l] != s[r]:
                return (pal(l +1, r) or pal(l, r -1))
            
            l+= 1
            r -=1
        return True

    
    def isAl(self, l):
        if (ord(l) >= ord("a") and ord(l) <= ord("z"))\
        or (ord(l) >= ord("A") and ord(l)<= ord("Z"))\
        or (ord(l) >= ord("0") and ord(l)<= ord("9")):
            return True
        
        