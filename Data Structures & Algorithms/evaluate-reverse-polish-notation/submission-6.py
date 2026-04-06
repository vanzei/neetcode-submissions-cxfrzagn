class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                newValue = stack.pop() + stack.pop()
                stack.append(int(newValue))
            elif token == "*":
                newValue = stack.pop() * stack.pop()
                stack.append(int(newValue))
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                newValue = b - a
                stack.append(int(newValue))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                newValue = b / a
                stack.append(int(newValue))
            else:
                stack.append(int(token))
        return int(stack[-1])

