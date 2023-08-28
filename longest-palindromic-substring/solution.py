class Solution:
    def longestPalindrome(self, s: str) -> str:
        LEN = len(s)
        max_palindrome = ""
        for i, c in enumerate(s):
            p1 = self.find_palindrome(s, i, i, LEN)
            p2 = self.find_palindrome(s, i, i + 1, LEN)
            if len(p1) > len(max_palindrome):
                max_palindrome = p1
            if len(p2) > len(max_palindrome):
                max_palindrome = p2

        return max_palindrome

    def find_palindrome(self, s, left, right, length):

        if left >= 0 and right < length and s[left] != s[right]:
            return ""

        while left >= 0 and right < length and s[left] == s[right] and left - 1 >= 0 and right + 1 < length and s[
            left - 1] == s[right + 1]:
            left -= 1
            right += 1
        temp = s[left:right + 1]
        return temp