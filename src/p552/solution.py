class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        import numpy as np
        dp = np.zeros((3, 3, 2), dtype=int)
        # dp = [[[0] * 2 for j in range(3)] for i in range(n)]
        dp[0][0][0] = 0  # 'A' -> 0
        dp[0][0][1] = 1  # 'A' -> 1
        dp[0][1][0] = 1  # 'P'
        dp[0][1][1] = 0
        dp[0][2][0] = 1  # 'L'
        dp[0][2][1] = 0
        a, b, c = -2, -1, 0
        for i in range(1, n):
            a += 1
            b += 1
            c += 1
            if i > 1:
                a %= 3
            b %= 3
            c %= 3

            dp[c][0][1] = (dp[b][1][0] + dp[b][2][0]) % mod
            dp[c][1][0] = (dp[b][1][0] + dp[b][2][0]) % mod
            dp[c][1][1] = (dp[b][0][1] + dp[b][1][1] + dp[b][2][1]) % mod
            dp[c][2][0] = (dp[b][1][0] + (1 if i == 1 else dp[a][1][0])) % mod
            dp[c][2][1] = (dp[b][0][1] + dp[b][1][1] + (
                0 if i == 1 else (dp[a][0][1] + dp[a][1][1]))) % mod
            # print(dp[i])
        return (int)((dp[c][0][0] + dp[c][0][1] + dp[c][1][0] + dp[c][1][1] + dp[c][2][0] + dp[c][2][
            1]) % mod)


if __name__ == '__main__':
    print(Solution().checkRecord(100000))
