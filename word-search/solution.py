from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        result = set()

        target_len = len(word)

        def dfs(r, c, i):

            if i == target_len:
                return True

            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited\
                    or word[i] != board[r][c]:
                return
            visited.add((r,c))
            res = dfs(r +1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c + 1, i+1) or dfs(r, c - 1, i+1)
            visited.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

if __name__ == '__main__':
    s = Solution()
