import heapq
from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [[grid[0][0], 0, 0]]
        max_val = grid[0][0]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = set()

        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            max_val = max(val, max_val)
            if r == ROWS - 1 and c == COLS-1:
                break
            for dx, dy in directions:
                tx, ty = r+dx, c+dy
                if 0 <= tx < ROWS and 0 <= ty < COLS and (tx,ty) not in visited:
                    heapq.heappush(min_heap, [grid[tx][ty], tx, ty])
                    visited.add((tx,ty))
        return max_val


if __name__ == '__main__':
    s = Solution()
