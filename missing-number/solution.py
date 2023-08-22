from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = 0
        for i in range(LEN + 1):
            res = res ^ i
            if i < LEN:
                res = res ^ nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
