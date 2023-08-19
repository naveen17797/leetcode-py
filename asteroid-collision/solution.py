from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = asteroid + stack[-1]
                if diff < 0:
                    # new asteroid won, pop the stack
                    stack.pop()
                elif diff > 0:
                    # existing asteroid won
                    asteroid = 0
                else:
                    # both are equal
                    stack.pop()
                    asteroid = 0
            # after all collisions a asteroid might exist
            if asteroid:
                stack.append(asteroid)

        return stack