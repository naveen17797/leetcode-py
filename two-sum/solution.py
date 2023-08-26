from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [index, cache.get(diff)]
            else:
                cache[num] = index
