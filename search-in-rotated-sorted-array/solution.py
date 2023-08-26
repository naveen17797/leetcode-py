from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        start,end = 0, LEN - 1
        while start <= end:
            mid = start + ( (end-start) // 2)
            # check which half is sorted
            # the logic is we will keep dividing until we find the element
            if nums[mid] == target:
                return mid
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end

            if  nums[start] <= nums[mid]:
                # we still need to check if the target is in range
                if target > nums[start] and target < nums[end]:
                    # target lies in the sorted half
                    end = mid
                else:
                    start = mid + 1
            else:
                # we still need to check if the target is in range
                if target > nums[mid] and target < nums[end]:
                    # mid to end is sorted half
                    start = mid + 1
                else:
                    end = mid
        return -1
