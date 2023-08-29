from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0 , len(numbers)
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l,r]
            if sum < target:
                r -= 1
            else:
                l += 1
