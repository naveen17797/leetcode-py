from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(i, curr, a):
            if len(curr) > k or a > n:
                return
            if len(curr) == k and a == n:
                result.append(list(curr))
                return

            for i in range(i, 10):
                curr.append(i)
                backtrack(i+1, curr, a + i)
                curr.pop()

        backtrack(1, [], 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3,7))