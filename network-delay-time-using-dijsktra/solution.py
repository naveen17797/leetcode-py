import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, time_took_to_reach_parent_vertex in times:
            graph[u].append([time_took_to_reach_parent_vertex, v])

        result = [float("+inf")] * n
        result[k - 1] = 0
        visited = set()
        visited.add(k)

        min_heap = [[0,k]]

        while min_heap:
            time_took_to_reach_parent_vertex, parent_vertex = heapq.heappop(min_heap)

            result[parent_vertex - 1] = min(result[parent_vertex - 1], time_took_to_reach_parent_vertex)

            for connected_vertex_time, connected_vertex in graph[parent_vertex]:
                total_time = time_took_to_reach_parent_vertex + connected_vertex_time
                if total_time < result[connected_vertex-1]:
                    result[connected_vertex-1] = total_time
                    heapq.heappush(min_heap, [connected_vertex_time + time_took_to_reach_parent_vertex, connected_vertex])

        minimum_time_taken = max(result)
        return minimum_time_taken if minimum_time_taken != float("inf") else -1

if __name__ == '__main__':
    s = Solution()
    s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
