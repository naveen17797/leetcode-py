from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            if (r,c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prev_height:
                return
            visited.add((r,c))
            # search adjacent cells
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        # we approach from top and bottom
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS- 1, c, atl, heights[ROWS-1][c])

        #now we approach from left to right
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        return pac & atl


if __name__ == '__main__':
    s = Solution()
