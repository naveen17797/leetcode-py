from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        for idx, num in enumerate(nums):
            res = self.twoSum(nums[idx + 1:], -num)
            for item in res:
                result.add([num, nums[item[0]], nums[item[1]]])
        return list(result)

    def twoSum(self, nums: List[int], target: int):
        cache = {}
        indices = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                indices.append( [index, cache.get(diff)] )
            else:
                cache[num] = index

        return indices
