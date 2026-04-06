class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtracking(open, closed):
            if open == n and closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append('(')
                backtracking(open + 1, closed)
                stack.pop()
            if open > closed:
                stack.append(')')
                backtracking(open, closed+1)
                stack.pop()

        backtracking(0, 0)
        return res




        