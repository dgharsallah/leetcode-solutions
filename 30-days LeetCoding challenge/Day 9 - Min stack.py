class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.minStack.append(min(self.minStack[-1] if len(self.minStack) > 0 else 1e18, x))
            
    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
