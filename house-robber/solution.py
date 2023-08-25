from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = [0] * (LEN + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, LEN):
            dp[i + 1] = max( dp[i], dp[i-1] + nums[i])

        return dp[LEN]
