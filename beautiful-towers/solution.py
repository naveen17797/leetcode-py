from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = min(maxHeights[0], 1)

        for i in range(1, n):
            left_max[i] = min(maxHeights[i], left_max[i - 1] + 1)

        right_max[n - 1] = min(maxHeights[n - 1], 1)

        for i in range(n - 2, -1, -1):
            right_max[i] = min(maxHeights[i], right_max[i + 1] + 1)

        max_sum = 0

        for i in range(n):
            max_sum += max(0, min(left_max[i], right_max[i]))

        return max_sum
if __name__ == '__main__':
    s = Solution()
    print(s.maximumSumOfHeights([5,3,4,1,1]))