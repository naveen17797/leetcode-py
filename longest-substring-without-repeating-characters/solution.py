class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        LEN = len(s)
        window_start, window_end = 0, 0
        max_len = 0
        frequency_set = set()
        while window_start <= window_end and window_end < LEN:
            if s[window_end] in frequency_set:
                # then we have to move start pointer until s[window_end] not in frequency set
                while s[window_end] in frequency_set and window_start <= window_end:
                    frequency_set.remove(s[window_start])
                    window_start += 1
                # once the above loop is executed
                # there may be two possibilities
                # 1. we will have no elements in the set
                # 2. we will have elements in the set
                # if we have elements we dont need to set the max in the first condition
                # the reason we dont do that is because we would already set the max for string x
                # as we move the start pointer this length of string x keeps on decreasing
                # so the max has to be set on else branch, because if we encounter a new character
                # there is a chance of growth, thats where we set the max not when we reducing it
            else:
                frequency_set.add(s[window_end])
                max_len = max(max_len, window_end - window_start + 1)
                window_end += 1

        return max_len




if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
