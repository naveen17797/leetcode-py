import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        to_visit = set([tuple(point) for point in points])
        priority_queue = [(0, tuple(points[0])) ]
        min_cost = 0
        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)
            if current_node not in to_visit: continue
            min_cost += current_cost
            to_visit.remove(current_node)
            priority_queue = []
            if len(to_visit) == 0: break
            for node in to_visit:
                distance = abs(node[0] - current_node[0]) + abs(node[1] - current_node[1])
                heapq.heappush(priority_queue, (distance, node))

        return min_cost

if __name__ == '__main__':
    s = Solution()
    res = s.minCostConnectPoints([[3,12],[-2,5],[-4,1]])
    print(res)
