class MinStack:

    def __init__(self):
        self.main = []
        self.min_stack = []


    def push(self, val: int) -> None:
        if self.min_stack:
            self.min_stack.append( val if val < self.min_stack[-1] else self.min_stack[-1])
            self.main.append(val)
        else:
            self.min_stack.append(val)
            self.main.append(val)


    def pop(self) -> None:
        self.min_stack.pop()
        return self.main.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
