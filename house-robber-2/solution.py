from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            self.compute(nums[1:]),
            self.compute(nums[:1])
        )

    def compute(self, nums:List[int]) -> int:
        LEN = len(nums)
        if not LEN: return 0
        dp = []
        dp[0] = 0
        dp[1] = 1
        for i in range(1, LEN):
            dp[i + 1] = max( dp[i], dp[i-1] + nums[i])

        return dp[LEN]

