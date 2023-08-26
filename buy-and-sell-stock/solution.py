from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)
        if len == 1: return 0

        local_min = prices[0]
        max_profit = 0

        for i in range(LEN):
            profit = prices[i] - local_min
            if profit <= 0:
                local_min = prices[i]
            max_profit = max(max_profit, profit)
        return max_profit