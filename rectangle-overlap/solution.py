class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        a1,b1,a2,b2 = rec2

        if x2<=a1 or x1>=a2:
            return False
        if y1>=b2 or y2<=b1:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
