from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        LEN = len(nums)
        start, end = 0, LEN - 1

        if LEN == 1 and nums[0] == target:
            return [0,0]

        while start <= end:
            mid = start + ((end - start) // 2)

            if nums[mid] == target:
                return self.get_start_and_end_pos(mid, nums, LEN, target)

            if nums[start] <= target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        return [-1, -1]

    def get_start_and_end_pos(self, mid, nums, length, target):
        # we may go fwd or backward from mid, we might very well do both
        left = mid
        right = mid

        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1

        while right + 1 < length and nums[right + 1] == target:
            right += 1

        return [left, right]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1,4], 4))
