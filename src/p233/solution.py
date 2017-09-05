class Solution(object):
    def C(self, n, m):
        if self.c[n][m]:
            return self.c[n][m]
        if n == m or m == 0:
            self.c[n][m] = 1
        else:
            self.c[n][m] = self.C(n - 1, m) + self.C(n - 1, m - 1)
        return self.c[n][m]

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        self.c = [[0] * 32 for _ in range(32)]
        result = 0
        l = []
        while n:
            l.append(n % 10)
            n //= 10
        l.reverse()
        ones = 0
        for i, digit in enumerate(l):
            rear_digits_num = len(l) - i - 1
            if digit >= 2:
                result += (digit - 1) * sum(
                    (count + ones) * self.C(rear_digits_num, count) * 9 ** (rear_digits_num - count) for count in
                    range(rear_digits_num + 1))
                result += sum(
                    (count + ones + 1) * self.C(rear_digits_num, count) * 9 ** (rear_digits_num - count) for count
                    in range(rear_digits_num + 1))
            elif digit == 1:
                result += sum((count + ones) * self.C(rear_digits_num, count) * 9 ** (rear_digits_num - count) for
                              count in range(rear_digits_num + 1))
            if digit == 1:
                ones += 1
        return result + sum((x == 1 for x in l))


print(Solution().countDigitOne(20))
