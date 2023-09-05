from typing import List


class TrieNode:
    def __init__(self, is_end_of_word = False):
        self.is_end_of_word = is_end_of_word
        self.children = {}
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_of_word = True

    def remove_word(self, word):
        curr = self
        for c in word:
            if len(curr.children[c].children) == 0:
                del curr.children[c]
                return
            else:
                curr = curr.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] not in node.children:
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_end_of_word:
                res.add(word)
            dfs( r + 1, c, node, word)
            dfs( r - 1, c, node, word)
            dfs( r, c + 1, node, word)
            dfs( r, c-1, node, word)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")

        return list(res)




if __name__ == '__main__':
    s = Solution()
