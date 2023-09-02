from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow, slow2 = 0,0,0
        while True:
            # the indexes of array has values which will again point it to
            # index with in array, this allows us to detect a cycle with
            # floyds algorithm
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # break at first intersection

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow


if __name__ == '__main__':
    s = Solution()
