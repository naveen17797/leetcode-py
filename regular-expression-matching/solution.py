class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_len = len(p)
        s_len = len(s)
        cache = {}

        def dfs(i, j):
            nonlocal cache
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= s_len and j >= p_len:
                return True
            # couldn't match the pattern ( insufficient )
            if j >= p_len:
                return False
            is_match =  (i < s_len) and ( s[i] == p[j]  or p[j] == ".")
            if (j+1) < p_len and p[j+1] == "*":
                # we have two choices, we can use * or we skip the char
                cache[(i,j)]  = dfs(i, j+2) or (is_match and dfs(i+1,j))
                return cache[(i,j)]

            if is_match:
                # we dont have a star, just proceed
                cache[(i, j)] = dfs(i+1, j+1)
                return  cache[(i,j)]

            cache[(i, j)] = False
            return cache[(i, j)]
        return dfs(0,0)