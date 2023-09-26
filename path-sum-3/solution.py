from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        # for each node we take right and left sum and return it
        res = float("-inf")

        def path_sum(node):
            right = path_sum
