import functools


class Solution:
    mod = 10 ** 9 + 7

    def add(self, *args):
        return functools.reduce(lambda a, b: (a + b) % self.mod, args, 0)

    def mul(self, *args):
        return functools.reduce(lambda a, b: a * b % self.mod, args, 1)

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        s = '0' + s
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        dp[1] = 9 if s[1] == '*' else 1
        for i in range(2, n):
            if s[i] == '0':
                if s[i - 1] == '*':
                    dp[i] = self.mul(dp[i - 2], 2)  # s[i-1] can only be 1 or 2
                elif s[i - 1] in '12':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i] in '123456':
                if s[i - 1] == '*':
                    dp[i] = self.add(dp[i - 1], self.mul(dp[i - 2], 2))  # s[i-1] can only be 1 or 2
                elif s[i - 1] in '12':
                    dp[i] = self.add(dp[i - 1], dp[i - 2])
                else:
                    dp[i] = dp[i - 1]
            elif s[i] in '789':
                if s[i - 1] == '*':
                    dp[i] = self.add(dp[i - 1], dp[i - 2])  # s[i-1] can only be 1
                elif s[i - 1] == '1':
                    dp[i] = self.add(dp[i - 1], dp[i - 2])
                else:
                    dp[i] = dp[i - 1]
            else:
                if s[i - 1] == '*':
                    dp[i] = self.add(self.mul(dp[i - 1], 9), self.mul(dp[i - 2], 15))  # get rid of 0*, 10 and 20
                elif s[i - 1] == '0':
                    dp[i] = self.mul(dp[i - 1], 9)
                elif s[i - 1] == '1':
                    dp[i] = self.add(self.mul(dp[i - 1], 9), self.mul(dp[i - 2], 9))  # s[i] can be '123456789'
                elif s[i - 1] == '2':
                    dp[i] = self.add(self.mul(dp[i - 1], 9), self.mul(dp[i - 2], 6))  # s[i] can be '123456'
                else:
                    dp[i] = self.mul(dp[i - 1], 9)
        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().numDecodings('1*'))
