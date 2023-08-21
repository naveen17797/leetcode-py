class ListNode:
    def __init__(self, val,  prev, nxt):
        self.val = val
        self.prev = prev
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = ListNode(value, self.right.prev, self.right)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space -= 1
        return True
    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.next.val
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.prev.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0
