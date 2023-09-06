class Solution:
    def countSubstrings(self, s: str) -> int:
        LEN = len(s)
        count = 0

        def count_palindrome(start, end):
            c = 0
            while start >= 0 and end < LEN and s[start] == s[end]:
                c += 1
                start, end = start - 1, end + 1
            return c


        for i in range(LEN):
            count += count_palindrome(i, i)
            count += count_palindrome(i , i+1)
        return count



