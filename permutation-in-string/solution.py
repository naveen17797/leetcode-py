class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_frequency_map = {}
        target_len = len(s1)
        for c in s1:
            target_frequency_map[c] = target_frequency_map.get(c, 0) + 1

        window_start, window_end = 0, 0
        LEN = len(s2)

        required_characters = target_len

        while window_end < LEN:
            char = s2[window_end]
            curr = s2[window_start:window_end]
            # decrement the frequency
            target_frequency_map[char] = target_frequency_map.get(char, 0) - 1

            if target_frequency_map[char] < 0:
                # move the starting window to end
                while target_frequency_map[char] != 0:
                    window_start_char = s2[window_start]
                    window_start += 1
                    target_frequency_map[window_start_char] += 1


            if window_end - window_start + 1 == target_len:
                return True
            window_end += 1

        return False

if __name__ == '__main__':
    s = Solution()
    s.checkInclusion("adc", "dcda")
