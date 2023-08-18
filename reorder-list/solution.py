# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head

        if not head.next:
            return

        fast = head.next.next
        h1 = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse list at mid..end
        second = self.reverseList(slow.next)

        # detach link at 0..mid
        slow.next = None

        first = head

        while first.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        first.next = second

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            # severe connection with next node
            head.next = prev
            # set previous node to head
            prev = head
            # now move the head to tmp
            head = tmp

        head = prev

        return head