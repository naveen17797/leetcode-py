class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s.lower() if ch.isalnum())

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return end - start <= 1