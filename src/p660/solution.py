class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = []
        while n != 0:
            l.append(n % 9)
            n //= 9
        l.reverse()
        return int(''.join(l))
