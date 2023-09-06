from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res

        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r,c,-1))
        return max_path

if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))