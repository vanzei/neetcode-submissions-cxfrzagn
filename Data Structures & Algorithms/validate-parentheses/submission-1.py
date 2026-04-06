class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapX = { "}": "{", "]":"[",")":"("}

        for x in s:
            if x in ["[", "{","("]:
                stack.append(x)
            else:
                if stack and stack[-1] == mapX[x]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0