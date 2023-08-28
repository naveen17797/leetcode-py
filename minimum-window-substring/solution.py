class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start, window_end = 0, 0
        LEN = len(s)

        target_frequency = {}
        for c in t:
            target_frequency[c] = target_frequency.get(c, 0) + 1

        min_substring = ""
        min_substring_len = float("+inf")
        required_character_count = len(t)

        while window_start <= window_end and window_end < LEN:
            char = s[window_end]

            if target_frequency.get(char, 0) > 0:
                required_character_count -= 1

            # decrement frequency
            target_frequency[char] = target_frequency.get(char, 0) - 1
            # [ADOBECODEBANC]
            # [ADOBEC]
            while required_character_count == 0 and window_start <= window_end:
                # move the window_start to window_end
                curr = s[window_start:window_end+1]
                curr_char = s[window_start]

                if len(curr) < min_substring_len:
                    min_substring_len = len(curr)
                    min_substring = curr
                if target_frequency[curr_char] >= 0:
                    required_character_count += 1

                # we would also need to add it to frequency map since the character is being removed
                target_frequency[curr_char] =  target_frequency.get(curr_char, 0) + 1
                window_start += 1
            window_end += 1
        return min_substring

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
