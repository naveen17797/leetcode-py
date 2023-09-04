from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cumulative_sum, count = 0,0
        prefix_map = {0:1}
        for num in nums:
            cumulative_sum += num
            if cumulative_sum - k in prefix_map:
                count += prefix_map.get(cumulative_sum % k, 0)
            prefix_map[cumulative_sum] = prefix_map.get(cumulative_sum, 0) + 1
        return count

if __name__ == '__main__':
    s = Solution()
