from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, is_buying):
            if i >= len(prices):
                return 0
            if (i, is_buying) in cache:
                return cache[(i, is_buying)]
            cooldown = dfs(i + 1, is_buying)
            if is_buying:
                buy = dfs(i+1, not is_buying) - prices[i]
                cache[(i, is_buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not is_buying) + prices[i]
                cache[(i, is_buying)] = max(sell, cooldown)

            return cache[(i, is_buying)]

        return dfs(0,True)


if __name__ == '__main__':
    s = Solution()
