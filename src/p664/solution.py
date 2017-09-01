class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(s)
        memo = {}

        def dp(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[left, right]

            index = right
            while s[index] == s[right] and index >= left:  # for speeding up
                index -= 1
            ans = dp(left, index) + 1
            for i in range(left, index):
                if s[i] == s[right]:
                    # dp(left, i) is similar to treat all the characters from the
                    # rear which are equal to s[i] by the first step
                    ans = min(ans, dp(left, i) + dp(i + 1, index))
            memo[left, right] = ans
            return ans

        return dp(0, n - 1)
