from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0 # keep track of iteration sum
        max_sum = float("-inf") # keep track of max sum


        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        return max_sum