from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
        return min( cost[len(cost) -2], cost[len(cost) - 1])




if __name__ == '__main__':
    s = Solution()
    s.minCostClimbingStairs([10,15,20])
