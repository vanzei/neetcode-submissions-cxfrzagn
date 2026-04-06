class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        value = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return value

    def peek(self) -> int:
        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        value = self.stack[-1]
        while self.temp:
            self.stack.append(self.temp.pop())
        return value
        

    def empty(self) -> bool:
        print(self.stack)
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()