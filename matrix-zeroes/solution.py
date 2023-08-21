from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][c] = None

        # now that we marked every cell, we just need to set zeroes

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] is None:
                    for i in range(max(ROWS, COLS)):
                        if i < ROWS and matrix[i][c] is not None:
                            matrix[i][c] = 0
                        if i < COLS and matrix[r][i] is not None:
                            matrix[r][i] = 0
                    matrix[r][c] = 0


if __name__ == "__main__":
    s = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)
