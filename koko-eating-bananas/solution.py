from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        min_k = float("+inf")

        def can_eat_in_time(speed):
            hours = 0
            for pile in piles:
                q = int(pile / speed)
                hours += q
                if pile % speed != 0:
                    hours += 1
            return hours <= h


        while start <= end:
            mid = start + ((end-start) // 2)
            if can_eat_in_time(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start





if __name__ == '__main__':
    s = Solution()
    s.minEatingSpeed([3,6,7,11], 8)
