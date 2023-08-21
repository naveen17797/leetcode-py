class Solution:
    def calculate(self, s: str) -> int:
        output, cur, sign, stack = 0,0,1,[]
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
                # use curr to keep track of a digit, but dont consume it yet unless you receive a operator or bracket
            elif c in "+-":
                output += (cur*sign)
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ")":
                output += (cur*sign)
                output *= stack.pop()
                output += stack.pop()
                cur = 0

        return output + (cur*sign)

if __name__ == "__main__":
    s = Solution()
    s.calculate("2 - (3+2)")

