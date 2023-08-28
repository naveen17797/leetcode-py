class ListNode:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next



class LRUCache:


    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            # we need to delete the node and add it before head
            node = self.map[key]
            self.remove_node(node)
            self.map[key] = self.add_node(ListNode(key, node.value))
            return self.map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            new_node = self.add_node( ListNode(key, value) )
            self.map[key] = new_node
        else:
            if len(self.map) == self.capacity:
                node_to_be_removed = self.tail.prev
                self.remove_node(node_to_be_removed)
                self.map.pop(node_to_be_removed.key)
            self.map[key] = self.add_node( ListNode(key, value) )


    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_node(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        return node



if __name__ == '__main__':
    s = Solution()
