class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = self.merge_intervals(points)

        return len(points)

    def merge_intervals(self, intervals):
        intervals.sort(key=lambda x: x[0])
        stack = []
        for start, end in intervals:
            if len(stack) == 0:
                stack.append([start, end])
            else:
                # check if overlap or not
                old_start, old_end = stack[-1]

                if start <= old_end:
                    stack[-1] = [max(start, old_start), min(end, old_end)]
                else:
                    stack.append([start, end])
        return stack
