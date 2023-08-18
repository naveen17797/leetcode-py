from typing import Optional


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head is not None:
            tmp = head.next
            # severe connection with next node
            head.next = prev
            # set previous node to head
            prev = head
            # now move the head to tmp
            head = tmp

        head = prev

        return head