class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        # only add parenthesis if open < n


        # only add closing if closed < open
    
        # valid if open == closed == n
        def backtrack(nOpen, nClose, n):
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen +1, nClose, n)
                stack.pop()
            if nClose < nOpen:
                stack.append(")")
                backtrack(nOpen, nClose + 1, n)
                stack.pop()
            if nClose == nOpen == n:
                res.append("".join(stack))
        backtrack(0,0,n)
        return res


