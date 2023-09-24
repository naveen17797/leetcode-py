class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = len([char for char in s if char == '1'])

        zeroes = len(s) - ones
        # "0101"  ones = 2 zeroes = 2
        # to make odd binary we would always need to set the last bit
        res = "1"
        ones -= 1
        # lets add zeroes before res
        res = ("0" * zeroes) + res
        res = ("1" * ones) + res
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maximumOddBinaryNumber("0101"))