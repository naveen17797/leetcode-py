import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        temp = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            temp[value].append(key)

        res = []
        for i in range(len(temp) - 1, 0, -1):
            for item in temp[i]:
                res.append(item)
                if len(res) == k:
                    return res



if __name__ == '__main__':
    s = Solution()
