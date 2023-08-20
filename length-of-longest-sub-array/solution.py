from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        window_start = 0
        frequency_dict = {}
        frequency_dict = defaultdict(lambda: 0, frequency_dict)
        max_arr = 0
        max_frequency = 0

        for window_end, value in enumerate(nums):
            frequency_dict[value] += 1
            max_frequency = max(max_frequency, frequency_dict[value])
            while window_end - window_start - max_frequency + 1 > k:
                frequency_dict[nums[window_start]] -= 1
                window_start += 1
            max_arr = max(max_arr, max_frequency)

        return max_arr


if __name__ == "__main__":
    s = Solution()
    print(s.longestEqualSubarray([1,3,2,3,1,3], 3))
