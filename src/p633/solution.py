class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        sqrt_c = math.floor(math.sqrt(c))
        for a in range(sqrt_c + 1):
            b = c - a ** 2
            sqrt_b = math.floor(math.sqrt(b))
            if sqrt_b ** 2 * 1.0 == b:
                return True
        return False
