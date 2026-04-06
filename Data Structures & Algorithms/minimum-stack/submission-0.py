class MinStack:

    def __init__(self):
        self.stack = []
        self.minP = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minP and val < self.minP[-1]:
            self.minP.append(val)
        elif not self.minP:
            self.minP.append(val)
        else:
            self.minP.append(self.minP[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minP.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minP[-1]
