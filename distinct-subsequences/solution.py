class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        s_len, t_len = len(s), len(t)

        def dfs(i, j):
            if j == t_len:
                return 1
            if i == s_len:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            # if characters match, then we have two options
            # match the character or ignore the character and try to match the next
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # if they dont match the only way is to look forward
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]
        modulo = 10 ** 9 + 7
        return dfs(0, 0) % modulo


if __name__ == '__main__':
    s = Solution()
