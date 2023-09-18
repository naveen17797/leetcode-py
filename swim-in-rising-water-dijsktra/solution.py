from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        output = 0
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        directions = [ [-1,0], [1,0], [0,1], [0,-1] ]

        ROWS, COLS = len(grid), len(grid[0])

        while min_heap:
            height, r, c = heappop(min_heap)
            output = max(output, height)
            if r == ROWS -1 and c == COLS - 1:
                break

            for dx, dy in directions:
                rx, cy = r + dx, c + dy
                if 0 <= rx < ROWS and 0 <= cy < COLS and (rx, cy) not in visited:
                    heappush(min_heap, (grid[rx][cy], rx, cy))
                    visited.add((r,c))
        return output




if __name__ == '__main__':
    s = Solution()
