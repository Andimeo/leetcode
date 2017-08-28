class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
        import itertools
        return sum(itertools.chain(*dp))