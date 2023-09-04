from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        stack = []
        for position, speed in sorted(pairs)[::-1]:
            stack.append( (target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



if __name__ == '__main__':
    s = Solution()
