from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node: Optional[TreeNode]) -> int:
            return 1 + max(depth(node.left), depth(node.right)) if node else 0
        return depth(root.left) + depth(root.right)