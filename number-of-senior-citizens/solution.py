from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                c += 1
        return c


if __name__ == '__main__':
    s = Solution()
