from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        LEN  = len(s)

        def is_palindrome(l,r):
            while l < r:
                if s[l] == s[r]:
                    l, r = l + 1, r - 1
                else:
                    return False
            return True


        def dfs(i):
            # reached end of string
            if i >= LEN:
                res.append(part.copy())
                return
            # aab
            for j in range(i, LEN):
                if is_palindrome(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res