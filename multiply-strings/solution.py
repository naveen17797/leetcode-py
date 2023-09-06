class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_max, num_min = (num2, num1) if len(num2) > len(num1) else (num1, num2)
        num_min = list(num_min)
        result = []
        place = 1
        while num_min:
            digit_2 = int(num_min.pop())
            num = ""
            carry = 0

            for i in range(len(num_max) - 1, -1, -1):
                digit_1 = int(num_max[i])
                product = carry + (digit_1 * digit_2)
                # two cases here
                # we have two digit number
                # we dont
                if product > 9:
                    carry = product // 10
                    num = str(product % 10) + num
                else:
                    carry = 0
                    num = str(product) + num

            if carry:
                num = str(carry) + num

            result.append(int(num) * place)
            place *= 10
        return str(sum(result))



if __name__ == '__main__':
    s = Solution()
    print(s.multiply("9", "99"))
