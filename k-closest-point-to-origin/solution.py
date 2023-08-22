import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for x,y in points:
            minHeap.append([(x ** 2 + y ** 2), x,y])
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res

if __name__ == '__main__':
    s = Solution()
