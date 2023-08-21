class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val >left):
                return False
            # check the child nodes
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        return validate(root, float("-inf"), float("+inf"))

if __name__ == '__main__':
    s = Solution()
