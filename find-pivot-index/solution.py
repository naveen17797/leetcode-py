from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        LEN = len(nums)
        right_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum -= num
            if right_sum == left_sum:
                return i
            left_sum += num
        return -1