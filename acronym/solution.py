from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        a = ""
        for word in words:
            a += word[0]

        return a == s

if __name__ == "__main__":
    s = Solution()
    print(s.isAcronym(["ali"]))


