from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = target
        x1_found, y1_found, z1_found = False, False, False
        for x1, x2, x3 in triplets:
            if x1 > t1 or x2 > t2 or x3 > t3:
                continue
            if x1 == t1:
                x1_found = True
            if x2 == t2:
                y1_found = True
            if x3 == t3:
                z1_found = True

            if x1_found and y1_found and z1_found: return True
        return False


if __name__ == '__main__':
    s = Solution()
