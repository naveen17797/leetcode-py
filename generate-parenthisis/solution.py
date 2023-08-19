from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", 0, 0, n, result)
        return  result

    def generate(self, curr:str, left:int, right:int, n:int, result:List[str]):
        if len(curr) == 2 * n:
            result.append(curr)
            return

        if left < n:
            self.generate(curr + "(", left + 1, right, n, result)

        if right < left:
            self.generate(curr+")", left, right + 1, n, result)

