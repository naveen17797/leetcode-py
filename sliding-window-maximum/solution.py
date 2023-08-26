import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque()
        for index, num in enumerate(nums):
            while q and q[-1] < index - k:
                # remove from end of q
                q.pop()

            # remove all elements less than new number
            while q and q[0] <= num:
                q.popleft()

            q.append(index)

            if  index - k >= 0:
                result.append(nums[q[0]])

        return result

