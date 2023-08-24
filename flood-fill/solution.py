import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image

        COLS = len(image[0])
        ROWS = len(image)
        start_color = image[sr][sc]
        visited = set()
        directions = [ [1,0], [-1,0], [0,1], [0,-1]]

        queue = collections.deque()
        queue.append((sr, sc))

        image[sr][sc] = color
        visited.add((sr, sc))

        while queue:
            r, c = queue.popleft()
            for direction in directions:
                dr, dc = direction
                tr, tc = r + dr, c + dc
                # check if inbounds
                if tr not in range(ROWS) or tc not in range(COLS):
                    continue
                # check if visited or of same color
                if (tr, tc ) in visited or  image[tr][tc] != start_color:
                    continue
                image[tr][tc] = color
                visited.add((tr, tc))
                queue.append((tr, tc))


        return image


if __name__ == '__main__':
    s = Solution()
