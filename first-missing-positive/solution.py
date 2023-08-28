from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 0
        LEN = len(nums)
        while start < LEN:
            value = nums[start]
            target_index = value - 1

            if target_index <= 0 and target_index < LEN and nums[target_index] != nums[start]:
                nums[start] = nums[target_index]
                nums[target_index] = value
            else:
                start += 1


        for i in range(LEN):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    s.firstMissingPositive([3, 4, -1, 1])
