from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        window_start = 0
        LEN = len(nums)

        number_of_ones = 0
        for window_end in range(LEN):

            if nums[window_end] == 1:
                number_of_ones += 1
            else:
                # not an one, shift window to window_end
                while window_start <= window_end:
                    if nums[window_start] == 1:
                        number_of_ones -= 1
                    window_start += 1

            if window_end - window_start + 1 == k and number_of_ones == k:
                return True

        return False

if __name__ == '__main__':
    s = Solution()
