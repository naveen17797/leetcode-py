class Solution:
    def fib(self, n: int, cache=[]) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if cache[n]:
            return cache[n]
        res = self.fib(n-1, cache) + self.fib(n-2, cache)
        cache[n] = res
        return res


if __name__ == '__main__':
    s = Solution()
