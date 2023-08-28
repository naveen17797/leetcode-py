from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = float("+inf")
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + ((end - start) // 2)
            target = min(nums[mid], target)
            target = min(nums[start], target)
            target = min(nums[end], target)
            if nums[start] <= nums[mid]:
                # start to mid is sorted
                start = mid + 1
            else:
                end = mid

        return target


if __name__ == '__main__':
    s = Solution()
    s.findMin([3,4,5,1,2])
