from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        LEN = len(nums)
        last_good_pos = nums[LEN -1] # point the end element to the last good pos
        for i in range(LEN-1, -1, -1):
            if i + nums[i] >= last_good_pos:
                last_good_pos = i

        return last_good_pos == 0


if __name__ == '__main__':
    s = Solution()
