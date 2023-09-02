class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = [(root, root.val)]
        count = 0
        while s:
            node, max_val = s.pop()
            if node.val >= max_val:
                count += 1
            if node.left:
                s.append((node.left, max(max_val, node.left.val)))
            if node.right:
                s.append((node.right, max(max_val, node.right)))
        return count



if __name__ == '__main__':
    s = Solution()
