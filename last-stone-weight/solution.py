import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            p1, p2 = -heapq.heappop(stones), -heapq.heappop(stones)

            diff = p1 - p2
            if diff:
                heapq.heappush(stones, -diff)
        stones.append(0)
        return -stones[0]

if __name__ == '__main__':
    s = Solution()
