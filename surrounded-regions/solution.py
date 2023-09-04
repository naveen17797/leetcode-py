from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        """
        Do not return anything, modify board in-place instead.
        """
        def capture(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "T"
                capture(r-1, c)
                capture(r+1, c)
                capture(r, c+1)
                capture(r, c-1)
            else:
                return

        # capture the regions on the border, because they will never be surrounded by X
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS-1] or c in [0, COLS-1]:
                    capture(r,c)

        # now capture the surrounded regions with x
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


if __name__ == '__main__':
    s = Solution()
