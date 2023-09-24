import math
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)

        visited = set()

        def dfs(parent, prime_count):
            if prime_count > 1:
                return 0

            total = 0
            for children in graph[parent]:
                total += dfs(children, prime_count + self.is_prime(children))





        for parent, childrens in graph.items():

            if self.is_prime(parent):
                childrens = [x for x in childrens if not self.is_prime(x)]
            else:
                childrens = [x for x in childrens if self.is_prime(x)]
            print(parent, childrens)
            for c in childrens:
                visited.add(tuple(sorted([parent, c])))



        print(visited)


    def is_prime(self,n):

        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.countPaths(5, [[1,2],[1,3],[2,4],[2,5]])
