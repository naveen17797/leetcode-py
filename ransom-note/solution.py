class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target_frequency = {}
        magazine_frequency = {}
        for c in ransomNote:
            target_frequency[c] = target_frequency.get(c, 0) + 1

        for c in magazine:
            magazine_frequency[c] = magazine_frequency.get(c, 0) + 1

        for c, value in target_frequency.items():
            if c not in magazine_frequency:
                return False
            if magazine_frequency[c] < value:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
