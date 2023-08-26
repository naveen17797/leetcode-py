from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        LEN = len(nums)
        answer = [1] * LEN

        # forward pass
        product = 1
        for i in range(LEN):
            answer[i] *= product
            product *= nums[i]

        # reverse pass
        product = 1
        for i in range(LEN - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer