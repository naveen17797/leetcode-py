from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # two steps

        # 1. transpose the matrix
        for i in range(N):
            for j in range(i, N):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # 2. reverse each row
        for i in range(N):
            for j in range(N//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][N-j-1]
                matrix[i][N-j-1] = temp



if __name__ == '__main__':
    s = Solution()
