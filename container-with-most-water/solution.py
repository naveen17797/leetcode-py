from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        LEN = len(height)
        i,j = 0, LEN - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area



if __name__ == '__main__':
    s = Solution()
