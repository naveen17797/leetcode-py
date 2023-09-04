class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max, left_min = 0, 0

        for c in s:
            if c == "(":
                left_max, left_min = left_max + 1, left_min + 1
            elif c == ")":
                left_max, left_min = left_max - 1, left_min - 1
            else:
                # asterik found, left max we consider that asterik to be open, left min we consider to be close char
                left_max, left_min = left_max + 1, left_min - 1

            if left_max < 0:
                return False

            if left_min < 0:
                # why ? take this string (**
                # left min will be -1, since we consider them as close characters
                left_min = 0
        return left_min == 0





if __name__ == '__main__':
    s = Solution()
