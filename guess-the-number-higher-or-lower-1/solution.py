# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start , end  = 0, n + 1
        while start < end:
            mid = start + ( (end-start) // 2)
            # check i to mid
            res =  guess(mid)
            if res == 0:
                return mid

            if res == -1:
                # number lies in i to mid
                end = mid
            else:
                start = mid + 1


    def guess(self, num:int) -> int:
        return 1