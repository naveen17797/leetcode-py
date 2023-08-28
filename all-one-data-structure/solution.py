class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = ListNode(0,0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            add_after = self.get_add_after(node.value + 1)
            self.remove_node(node)



    def dec(self, key: str) -> None:




    def is_empty(self):
        return self.head.next == self.tail

    def getMaxKey(self) -> str:
        if self.is_empty(): return ""
        return self.head.next.key

    def getMinKey(self) -> str:
        if self.is_empty(): return ""
        return self.tail.prev.key

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_node(self, node, add_after):
        temp = add_after.next
        add_after.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        return node


if __name__ == '__main__':
    s = Solution()
