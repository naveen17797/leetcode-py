class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        window_start, window_end = 0, 0
        LEN = len(s)
        majority_character_frequency = 0
        longest_repeating_letters = 0

        def number_of_replacements_needed():
            return window_end - window_start + 1 - majority_character_frequency

        while window_start <= window_end and window_end < LEN:
            char = s[window_end]
            frequency[char] = frequency.get(char, 0) + 1

            majority_character_frequency = max( majority_character_frequency, frequency[char])

            while number_of_replacements_needed() > k:
                window_start_char = s[window_start]
                # this means we have to move the start of the window
                frequency[window_start_char] -= 1
                window_start += 1
            longest_repeating_letters = max(longest_repeating_letters, window_end-window_start + 1)
            window_end += 1

        return longest_repeating_letters



if __name__ == '__main__':
    s = Solution()
