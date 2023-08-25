class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        dp = [0] *  LEN
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, LEN + 1):
            one = int(s[i-1:i])
            two = int(s[i-2:i])
            if one >= 1:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[LEN]
