class MinStack:

    def __init__(self):
        self.stack = []
        self.small = []
        

    def push(self, val: int) -> None:
        self.stack += [val]
        if len(self.stack)==1:
            self.small = [val]
        elif val<=self.small[-1]:
            self.small += [val]

    def pop(self) -> None:
        if len(self.stack)>0:
            if self.stack[-1]==self.small[-1]:
                del self.small[-1]
            del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.small[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()