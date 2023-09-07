from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        last_index_map = {}
        for i, c in enumerate(s):
            last_index_map[c] = i

        res = []

        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_index_map[c])
            if i == end:
                res.append(end-start + 1)
                start = end + 1
        return res



if __name__ == '__main__':
    s = Solution()
