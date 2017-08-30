class Solution:
    def read_num(self, s):
        sign = 1
        start = 0
        if s[start] in '+-':
            sign = -1 if s[start] == '-' else 1
            start += 1
        num = 0
        for i in range(start, len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
                continue
            if c == 'x':
                if i == 0 or s[i - 1] in '+-':
                    num = 1
                return sign * num, 1, i + 1
            else:
                return sign * num, 0, i
        return sign * num, 0, i + 1

    def get_coef(self, s):
        pos = 0
        coef, bias = 0, 0
        while True:
            num, x, next_pos = self.read_num(s[pos:])
            # print(num, x, next_pos)
            if x:
                coef += num
            else:
                bias += num
            pos += next_pos
            if pos == len(s):
                break
        return coef, bias

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        l_coef, l_bias = self.get_coef(left)
        # print(l_coef, l_bias)
        r_coef, r_bias = self.get_coef(right)
        # print(r_coef, r_bias)
        coef = l_coef - r_coef
        bias = r_bias - l_bias
        if coef == 0:
            if bias == 0:
                return "Infinite solutions"
            if bias != 0:
                return "No solution"
        return "x=%d" % (bias // coef)
