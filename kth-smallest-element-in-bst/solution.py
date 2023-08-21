from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur or stack:
            # keep going left, since in order traversal
            while cur:
                stack.append(cur)
                cur = cur.left

            # once we reach the end, then we pop the item from stack
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            # from the end node, check if we have right sub tree
            cur = cur.right
        return -1

if __name__ == '__main__':
    s = Solution()
