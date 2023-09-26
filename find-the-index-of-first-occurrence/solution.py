class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        needle_len, haystack_len = len(needle), len(haystack)
        while j < haystack_len:
            if haystack[j] == needle[i]:
                i += 1
            else:
                i = 0
            j += 1
            if i == needle_len - 1:
                return j  - needle_len + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
