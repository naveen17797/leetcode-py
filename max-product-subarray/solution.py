from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_product = float("-inf")
        LEN = len(nums)

        # left to right pass
        product = 1
        for i in range(LEN):
            product *= nums[i]
            max_product = max(max_product, product)
            if product == 0:
                product = 1


        # right to left pass
        product = 1
        for i in range(LEN - 1, -1, -1):
            product *= nums[i]
            max_product = max(max_product, product)
            if product == 0:
                product = 1


        return max_product
