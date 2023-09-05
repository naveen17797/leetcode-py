from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        group_prev = dummy_head
        # for example a sample list dummy -> 1 -> 2 -> 3 -> 4 -> 5
        while True:
            kth_node = self.kthNode(group_prev, k)
            if not kth_node:
                break
            # now we have the pointer landing at dummy -> 1 (ptr landed here) -> 2 -> 3 -> 4 -> 5
            group_next = kth_node.next # this now pointing to 2


            prev, curr = kth_node.next, group_prev.next # kth_node.next = 2, group_prev.next = 1
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reverse the list ( 1 -> 2 )

            # backup the first node in our group
            tmp = group_prev.next
            # now its set to ( 2 -> 1 )
            group_prev.next = kth_node
            group_prev = tmp
        return dummy_head.next

    def kthNode(self, head, k):
        while k and head:
            head = head.next
            k -= 1
        return head

if __name__ == '__main__':
    s = Solution()
