class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            factor <<= 1
        return m * factor
