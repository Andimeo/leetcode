class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # calculate how many numbers prefixed with n1
        def cal_step(n, n1, n2):
            k = 0
            while n1 <= n:
                k += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return k

        cur = 1
        k -= 1
        while k > 0:
            step = cal_step(n, cur, cur + 1)
            if step <= k:
                cur += 1
                k -= step
            else:
                k -= 1
                cur *= 10
        return cur
