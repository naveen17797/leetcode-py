class Solution:
    def parse_number(self, s):
        my_number = 0
        for c in s:
            if c.isnumeric():
                my_number = my_number * 10 + int(c)
        return my_number


if __name__ == '__main__':
    s = Solution()
    print(s.parse_number("23456"))
