from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_ocean_cells, atlantic_ocean_cells = set(), set()

        def dfs(r, c, prev_val, acc):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in acc or heights[r][c] < prev_val:
                return
            acc.add((r, c))
            val = heights[r][c]
            dfs(r + 1, c, val, acc)
            dfs(r, c + 1, val, acc)
            dfs(r - 1, c, val, acc)
            dfs(r, c - 1, val, acc)


        for i in range(ROWS):
            dfs(i, 0, -1, pacific_ocean_cells)
            dfs(i, COLS-1, -1, atlantic_ocean_cells)

        for j in range(COLS):
            dfs(0, j, -1, pacific_ocean_cells)
            dfs(ROWS-1, j, -1, atlantic_ocean_cells)

        return pacific_ocean_cells & atlantic_ocean_cells