class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            dp[i][0] = int(matrix[i][0] == '1')
        for i in range(m):
            dp[0][i] = int(matrix[0][i] == '1')
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        import itertools
        size = max(itertools.chain(*dp))
        return size ** 2
