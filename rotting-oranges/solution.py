import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time, fresh = 0,0

        ROWS, COLS = len(grid), len(grid[0])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r not in range(ROWS)
                            or c not in range(COLS) or
                            grid[r][c] != 1):
                        continue
                    # found a fresh cell to infect
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))

            time += 1

        return time if fresh == 0 else -1
