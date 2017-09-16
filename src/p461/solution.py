class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        result = 0
        while n:
            result += 1
            n &= n - 1
        return result
