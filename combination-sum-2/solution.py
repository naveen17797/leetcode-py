from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        LEN = len(candidates)


        def dfs(curr, start_from, total):

            if total == target:
                result.append(list(curr))
                return

            if total >= target:
                return

            prev = -1
            for i in range(start_from, LEN):
                if candidates[i] == prev:
                    continue # skip duplicates
                prev = candidates[i]
                curr.append(candidates[i])
                dfs(curr, i + 1, total + candidates[i])
                curr.pop()


        dfs([], 0, 0)
        return  result


if __name__ == '__main__':
    s = Solution()
