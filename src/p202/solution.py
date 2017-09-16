class Solution(object):
    def happy(self, n):
        l = []
        while n:
            l.append(n % 10)
            n /= 10
        return sum(x ** 2 for x in l)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        s = set()
        s.add(n)
        while True:
            n = self.happy(n)
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)
        return None
