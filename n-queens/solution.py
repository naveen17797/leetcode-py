class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]

        result = []
        positive_diag = set() # r + c
        negative_diag = set() # r - c
        columns = set()

        def solve(r):

            if r == n:
                return result.append([''.join(map(str, sub_list)) for sub_list in grid])

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

        return result