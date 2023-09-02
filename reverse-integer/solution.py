import collections
import math


class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        MAX = 2147483647
        MIN = -2147483648

        upper_limit = int(MAX/ 10)
        lower_limit = int(MIN/10)

        while x:
            rem = int(math.fmod(x, 10))

            if reversed > upper_limit or reversed == upper_limit and rem > 7: return 0
            if reversed < lower_limit or reversed == lower_limit and rem < -8: return 0

            x  = int(x/10)
            #123 ->  3, then 30 + 2 = 32, then 320 + 1 => 321
            reversed = (reversed * 10) + rem
        return reversed


if __name__ == '__main__':
    s = Solution()
