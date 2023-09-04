from collections import defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_map = defaultdict(lambda: 0)
        for task in tasks:
            frequency_map[task] += 1

        f = list(frequency_map.values())
        f.sort(reverse=True)

        max_value = f[0] - 1
        idle_slots = max_value * n

        for i in range(1, len(f)):
            idle_slots -= min(f[i], max_value)

        return len(tasks) + idle_slots if idle_slots > 0 else len(tasks)


if __name__ == '__main__':
    s = Solution()
