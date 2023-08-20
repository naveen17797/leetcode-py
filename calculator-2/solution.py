class Solution:
    def calculate(self, s: str) -> int:
        # get rid of spaces
        s = s.replace(" ", "")
        i = 0
        length = len(s)
        num = 0
        stack = []
        last_operation = "+"

        while i < length:
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            else:
                if last_operation == '+':
                  stack.append(num)
                elif last_operation == '-':
                    stack.append(-num)
                elif last_operation == '*':
                    stack.append(stack.pop() * num)
                elif last_operation == '/':
                    stack.append(int(stack.pop() / num))
                last_operation = s[i]
                # reset num to zeo
                num = 0
            i += 1

        if last_operation == '+':
            stack.append(num)
        elif last_operation == '-':
            stack.append(-num)
        elif last_operation == '*':
            stack.append(stack.pop() * num)
        elif last_operation == '/':
            stack.append(int(stack.pop() / num))



        res = 0
        for item in stack:
            res += item
        return res

if __name__ == "__main__":
    s = Solution()
    s.calculate(" 3 + 2 * 2 ")

