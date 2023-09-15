from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        LEN = len(startTime)

        def dp(a, i):
            if i >= LEN:
                return a


if __name__ == '__main__':
    s = Solution()
