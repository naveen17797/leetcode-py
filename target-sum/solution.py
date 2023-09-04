from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        LEN = len(nums)
        def dfs(i, total):


            if (i, total) in dp:
                return dp[(i, total)]

            if i == LEN:
                if total == target:
                    return 1
                return 0

            result = dfs( i + 1, total + nums[i]) + dfs( i + 1, total - nums[i] )
            dp[(i, total)] = result
            return result
        return dfs(0,0)



if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1,1,1,1,1], 3))

