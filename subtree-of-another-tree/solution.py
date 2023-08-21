# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, n1, n2):
        if n1 and n2:
            return n1.val == n2.val and self.is_same_tree(n1.left, n2.left) and self.is_same_tree(n1.right, n2.right)
        return n1 is n2


if __name__ == '__main__':
    s = Solution()
