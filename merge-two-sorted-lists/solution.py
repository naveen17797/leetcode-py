# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        start = head

        h1 = list1
        h2 = list2
        while h1 is not None and h2 is not None:
            # 1. we compare the node
            if h1.val <= h2.val:
                # detach the node
                tmp = h1
                head.next = tmp
                h1 = h1.next
            else:
                tmp = h2
                head.next = tmp
                h2 = h2.next
            head = head.next

        if h1 is not None:
            head.next = h1

        if h2 is not None:
            head.next = h2

        # position head to start of list
        return start.next

