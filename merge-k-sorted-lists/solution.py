# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            result = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                result.append(self.mergeTwo(l1, l2))

            # if we have 8 lists, this will be reduced to 4
            lists = result

        return lists[0]

    def mergeTwo(self, l1, l2):
        head = ListNode(0, None)
        start = head
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1

        if l2:
            head.next = l2

        return start.next



