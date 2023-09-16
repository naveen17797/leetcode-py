class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we
        LEN = len(temperatures)
        for i in range(LEN-1, -1, -1):
            while stack and stack[-1][0] < temperatures[i]:
                stack.pop()
            if not stack:
                res[i] = 0  # lets check if there are any elements
                stack.append([temperatures[i], i])  # add current element to stack
            else:
                res[i] = stack[-1][1] - i
                stack.append([temperatures[i], i])
        return res