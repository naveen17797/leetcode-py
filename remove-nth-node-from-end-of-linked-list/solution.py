from typing import Optional


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this node helps to find the node before our target node
        # without this we will land at the target node, where we cant perform removal
        dummy = ListNode(0, head)

        # initialize two pointers, we need to keep the distance
        # between two pointers to be K

        right = dummy
        left = dummy

        while n > 0 and right is not None:
            right = right.next
            n -= 1

        while right is not None:
            right = right.next
            left = left.next

        # now that we landed on the node, we can do the removal
        tmp = left.next
        if tmp is not None:
            tmp = tmp.next

        left.next = tmp

        return dummy.next

