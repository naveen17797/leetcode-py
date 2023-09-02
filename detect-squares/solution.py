from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []


    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py-y) != abs(px-x)) or x == px or y == py:
                continue
            res += self.pts_count[(x,py)] * self.pts_count[(px,y)]
        return res


if __name__ == '__main__':
    s = Solution()
