from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            # now check in 4 dirs
            return 1 + dfs(r-1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c-1)


        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))

        return max_area


if __name__ == '__main__':
    s = Solution()
