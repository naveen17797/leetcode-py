class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        left, curr_sum, max_len = 0, 0, 0
        if target == 0:
            return n
        for right, num in enumerate(nums):
            curr_sum += num
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if target == curr_sum:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len else -1


if __name__ == '__main__':
    s = Solution()
