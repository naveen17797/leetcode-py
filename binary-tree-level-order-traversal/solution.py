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
            if len(temp):
                # append vals to res
                res.append(self.vals(temp))
            temp = []
            for item in s:
                if item:
                    temp.append(item.left)
                    temp.append(item.right)
            s = temp
        return res


    def vals(self, l: List[TreeNode]):
        res = []
        for item in l:
            if item:
                res.append(item.val)
        return res

if __name__ == '__main__':
    s = Solution()
