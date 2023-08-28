from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        visited = {}

        def recurse(curr):
            if len(curr) == length:
                result.append(list(curr))
                return
            for num in nums:
                if num in visited:
                    continue
                curr.append(num)
                visited[num] = 1
                recurse(curr)
                curr.pop()
                visited.pop(num)

        recurse([])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
