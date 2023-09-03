from copy import deepcopy
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [["." for _ in range(n)] for _ in range(n)]

        total = 0



        result = []
        positive_diag = set() # r + c
        negative_diag = set() # r - c
        columns = set()

        def solve(r):
            nonlocal  total
            if r == n:
                total += 1
                return

            for c in range(n):
                if c not in columns and r+c not in positive_diag and r-c not in negative_diag and grid[r][c] != "Q":
                    columns.add(c)
                    positive_diag.add(r+c)
                    negative_diag.add(r-c)
                    grid[r][c] = "Q"

                    solve(r + 1)

                    grid[r][c] = "."
                    columns.remove(c)
                    positive_diag.remove(r+c)
                    negative_diag.remove(r-c)


        solve(0)

        return total


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
