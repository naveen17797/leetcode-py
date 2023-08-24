import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        directions = [
            [0, -1], [0, 1], [-1, 0], [1, 0]
        ]

        def bfs(r, c):
            visited.add((r, c))
            queue = collections.deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    tr = row + dr
                    tc = col + dc
                    # check bounds
                    if tr not in range(rows) or tc not in range(cols):
                        continue
                    # check if visited and skip
                    if (tr, tc) in visited:
                        continue
                    # there is no point in adding the node to bfs, if its a water
                    if grid[tr][tc] != "1":
                        continue
                    # if both conditions pass, then add it to queue
                    queue.append((tr, tc))
                    # we have visited this node
                    visited.add((tr, tc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


if __name__ == '__main__':
    s = Solution()
