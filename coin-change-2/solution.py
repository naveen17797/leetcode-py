from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LEN = len(coins)
        cache = {}
        def dfs(i,a):
            if a == amount: return 1
            if a > amount: return 0
            if i >= LEN: return 0
            if (i,a) in cache: return cache[(i,a)]
            cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return cache[(i,a)]
        return dfs(0,0)


if __name__ == '__main__':
    s = Solution()
    s.coinChange([1,2,5], 11)
