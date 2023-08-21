# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        depth = 0
        while stack:
            temp = []
            depth += 1
            for node in stack:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
            stack = [i for i in temp if i is not None]

        return depth



if __name__ == '__main__':
    s = Solution()
