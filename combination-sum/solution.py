from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        LEN = len(candidates)
        def dfs(i, total, curr):

            if total == target:
                result.append(list(curr))
                return

            if i >= LEN or total >= target:
                return

            curr.append(candidates[i])
            dfs(i, total + candidates[i], curr)
            curr.pop()
            dfs(i+1, total, curr)
        dfs(0, 0, [])
        return  result



if __name__ == '__main__':
    s = Solution()
