from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        start, end = 0, (ROWS * COLS) - 1

        while start <= end:
            mid = start + ((end-start) // 2)
            i, j = int(mid/COLS), int(mid % COLS)
            if target == matrix[i][j]:
                return True
            if matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

if __name__ == "__main__":
    s = Solution()
    s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)