from typing import Optional


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        j = head
        while j is not None and j.next is not None:
            head = head.next
            j = j.next.next
            if head == j:
                return True
        return False
