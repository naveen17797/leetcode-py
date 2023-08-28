from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0

        mul = 1
        while l1:
            n1 += mul * l1.val
            l1 = l1.next
            mul *= 10

        mul = 1
        while l2:
            n2 += mul * l2.val
            l2 = l2.next
            mul *= 10

        n3 = n1 + n2

        dummy = ListNode(0)

        if n3 == 0:
            return dummy

        head = dummy
        while n3:
            rem = n3 % 10
            n3 = (n3 // 10)
            head.next = ListNode(rem)
            head = head.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
