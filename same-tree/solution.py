from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [p, q]
        while stack:
            n1 = stack.pop()
            n2 = stack.pop()
            if n1 is None and n2 is not None:
                return False
            if n1 is not None and n2 is None:
                return False
            if n1 is None and n2 is None:
                continue

            if n1.val != n2.val:
                return False
            stack.append(n1.left)
            stack.append(n2.left)
            stack.append(n1.right)
            stack.append(n2.right)
        return True
