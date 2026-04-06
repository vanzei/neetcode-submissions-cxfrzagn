class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.maxC = 0
        self.cnt = {}

    def push(self, val: int) -> None:
        valCount = self.cnt.get(val, 0) + 1
        self.cnt[val] = valCount
        if valCount > self.maxC:
            self.maxC = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxC].pop()

        self.cnt[res] -= 1
        if not self.stacks[self.maxC]:
            self.maxC -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()