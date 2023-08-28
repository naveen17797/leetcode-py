from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        prime_dict = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
            'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
            'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101
        }

        target_product = 1
        # frequency map for target
        for c in p:
            target_product *= prime_dict[c]

        window_start, window_end = 0, 0
        LEN = len(s)
        indices = []

        current = 1
        while window_start <= window_end < LEN:
            char = s[window_end]
            current *= prime_dict[char]
            if current == target_product:
                indices.append(window_start)
            while current > target_product and window_start <= window_end:
                current = current // prime_dict[s[window_start]]
                window_start += 1
            window_end += 1
        return indices


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))