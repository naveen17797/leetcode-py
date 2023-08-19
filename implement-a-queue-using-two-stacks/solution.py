class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # but before doing this, we need to transfer all the values to stack s2
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        # now that we we put the value, transfer it back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0

