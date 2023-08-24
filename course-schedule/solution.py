from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visited = set()
        def can_be_completed(crs):
            if crs in visited:
                return False
            if len(pre_map[crs]) == 0:
                return True
            pres = pre_map[crs]
            visited.add(crs)
            for item in pres:
                if not can_be_completed(item):
                    return False
            visited.remove(crs)
            # if a course can be completed, then we can empty the array so we
            # can memorize it
            pre_map[crs] = []
            return True

        for crs, pre in prerequisites:
            if not can_be_completed(crs):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
