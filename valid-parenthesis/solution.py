class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        opening_brackets = brackets_map.keys()


        for character in s:
            if character in opening_brackets:
                stack.append(brackets_map[character])
            else:
                # we encountered a closing bracket
                # check if stack.pop() , if stack empty then return false
                if len(stack) == 0 or stack.pop() != character:
                    return False

        return len(stack) == 0