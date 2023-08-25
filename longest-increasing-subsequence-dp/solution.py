from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp  = [0] * (LEN+1)
        for i in range(LEN - 1, -1, -1):
            for j in range(i+1, LEN):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)


