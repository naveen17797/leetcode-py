import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:




    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = [root]
        res = []

        while s:
            temp = s
            # append vals to


        return res




if __name__ == '__main__':
    s = Solution()
