from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup[num] = 1

        return False
