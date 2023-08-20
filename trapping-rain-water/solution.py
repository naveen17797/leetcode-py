from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # it cant trap water on start, end of array since there is no wall to hold it
        # it can trap water in between blocks if this satisy condition
        # start_number <= end_number and end_block - start_block != 1 ( adjacent blocks cant trap water)
        # how do we actually calculate the water trapped ? ( aka area )
        # we need to do this only when start_block < current_block
        # the area would be (start_block - current_block) * 1

        #actual solution

        if not height:
            return 0

        total_area = 0

        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                total_area += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                total_area += max_right - height[r]


        return total_area




