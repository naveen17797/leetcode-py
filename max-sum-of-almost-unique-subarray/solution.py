from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # we definitely need a set to track number of unique elements which will be in current sub
        # array
        max_sum, current_sum = 0, 0
        window_start = 0
        LEN = len(nums)
        allowed_duplicate_values = k - m
        sub_array = []

        for window_end in range(LEN):

            current_sum += nums[window_end]
            sub_array.append(nums[window_end])

            if window_end - window_start + 1 == k:
                unique_list = [x for x in sub_array if sub_array.count(x) == 1]
                if len(unique_list) >= m:
                    max_sum = max(current_sum, max_sum)
                # now we move the window one step
                current_sum -= nums[window_start]
                sub_array.remove(nums[window_start])
                window_start += 1

        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSum([1,2,1,2,1,2,1], 3, 3))
