from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        queries_asc = sorted((q, i) for i, q in enumerate(queries))
        intervals.sort()

        i, num_intervals = 0, len(intervals)
        size_heap = []  # (size, left)

        for pos, qnum in queries_asc:

            while i < num_intervals:
                left, right = intervals[i]
                if left > pos:
                    break
                heapq.heappush(size_heap, (right - left + 1, left))
                i += 1

            while size_heap:
                size, left = size_heap[0]
                right = left + size - 1
                if right >= pos:
                    break
                heapq.heappop(size_heap)

            queries[qnum] = size_heap[0][0] if size_heap else -1

        return queries

if __name__ == '__main__':
    s = Solution()
