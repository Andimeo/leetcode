class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        if n == 0:
            return 0
        dp = [[1] + [0] * m for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[n][m]
