class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while ast < 0 and stack and stack[-1] > 0:
                result = ast + stack[-1]
                if result == 0:
                    ast = 0
                    stack.pop()
                elif result > 0:
                    ast = 0
                else:
                    stack.pop()
            if ast:
                stack.append(ast)
                
        return stack


