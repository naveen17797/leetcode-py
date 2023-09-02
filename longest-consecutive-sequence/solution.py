from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in set:
                temp = 1
                while num +1 in nums_set:
                    temp += 1
                longest_sequence = max(longest_sequence, temp)

        return longest_sequence



if __name__ == '__main__':
    s = Solution()
