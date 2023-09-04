from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, LEN, res = 0, 0, len(nums), 0
        while r < LEN - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            # adjust the boundary
            l = r + 1
            r = farthest
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
