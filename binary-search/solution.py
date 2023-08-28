from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + ( (end-start) // 2)
            if nums[mid] == target:
                return mid
            if nums[start] >= target and nums[mid] < target:
                end = mid
            else:
                start = mid + 1
        return -1

if __name__ == '__main__':
    s = Solution()
