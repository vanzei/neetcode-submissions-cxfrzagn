class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        reference = { "}":"{", ")":"(", "]":"["}

        for x in s:
            if stack and x in reference and reference[x] == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        
        return len(stack) == 0

                
