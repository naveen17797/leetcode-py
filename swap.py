class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        s1, s2 = list(s1), list(s2)


        if s1 == s2: return True
        combinations = []
        # swap 1 with 3

        combinations.append(self.swap(0,2, s1))
        combinations.append(self.swap(1,3, s1))
        combinations.append(self.swap(1,3, list(self.swap(0,2, s1))))

        # swap 0 with 2
        return ''.join(s2) in combinations


    def swap(self, i, j, l):
        l = l.copy()
        temp = l[j]
        l[j] = l[i]
        l[i] = temp
        return ''.join(l)


if __name__ == '__main__':
    s = Solution()
    print(s.canBeEqual("abcd", "cdab"))
