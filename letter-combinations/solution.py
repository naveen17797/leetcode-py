from typing import List

letters = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        length = len(digits)

        if length == 0: return result

        def recurse(start, curr):
            # base case
            if len(curr) == length:
                result.append(curr)
                return;


            # now that we have digit, get all letters bound to digit
            all_letters = letters[int(digits[start])]
            # now that we have all letters, lets loop through it to create a decision tree
            for letter in all_letters:
                # for each letter we need to do the same thing, browse the next letter
                recurse(start + 1, curr + letter)

        recurse(0, "")
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("234"))
