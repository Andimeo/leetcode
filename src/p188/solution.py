class Solution(object):
    """
     dp[i, j] represents the max profit up until prices[j] using at most i transactions.
     dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
              = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
     dp[0, j] = 0; 0 transactions makes 0 profit
     dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
    """

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not n or not k:
            return 0
        import math
        result = 0
        if k >= math.ceil(n / 2):
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    result += prices[i] - prices[i - 1]
            return result
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            local_max = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + local_max)
                local_max = max(local_max, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]
