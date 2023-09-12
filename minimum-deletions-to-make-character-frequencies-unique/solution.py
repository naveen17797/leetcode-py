from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        od = defaultdict(lambda: 0)
        for c in s:
            od[c] += 1

        frequency_set = set()

        res = 0

        for k, v in od.items():
            if v in frequency_set:
                while v in frequency_set:
                    v -= 1
                    res += 1
            if v > 0:
                frequency_set.add(v)
        return res

