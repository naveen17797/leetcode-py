"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        new_head = Node(-1)
        new_head_bk = new_head


        def may_be_get_node(node):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            return old_to_new[node]


        while head:

            #  check if same node not in our map
            if head not in old_to_new:
                old_to_new[head] = Node(head.val)

            # now time to copy the next node
            if head.next is not None:
                may_be_get_node(head.next)
                # now make connections to next
                old_to_new[head].next = old_to_new[head.next]

            # now time to copy the random node
            if head.random is not None:
                may_be_get_node(head.random)
                # now make connections to next and random
                old_to_new[head].random = old_to_new[head.random]

            new_head.next = old_to_new[head]
            new_head = new_head.next
            head = head.next

        return new_head_bk.next





if __name__ == '__main__':
    s = Solution()
