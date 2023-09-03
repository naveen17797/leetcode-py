class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []

        brackets_map = {
            '(': ')',
        }

        opening_brackets = brackets_map.keys()

        for i, character in enumerate(s):
            if character in opening_brackets:
                stack.append(brackets_map[character])
            elif character == "*":
                stack.append(character)
            else:

                # we encountered a closing bracket
                # check if stack.pop() , if stack empty then return false
                if len(stack) == 0:
                    return False



        stack = [i for i in stack if i != "*"]
        return len(stack) == 0
if __name__ == '__main__':
    s = Solution()
    p = s.checkValidString("()")
    print(p)
