class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 31
        count_0 = [0] * n
        count_1 = [0] * n
        count_0[0] = 1
        count_1[0] = 1
        for i in range(1, n):
            count_0[i] = count_0[i - 1] + count_1[i - 1]
            count_1[i] = count_0[i - 1]
        l = [0] * n
        numc = num
        for i in range(n):
            l[i] = numc & 1
            numc >>= 1
        is_consecutive = False
        for i in range(1, n):
            if l[i] == l[i - 1] == 1:
                is_consecutive = True
        result = 0
        for i in range(n - 1, -1, -1):
            if l[i] == 1:
                result += count_0[i]  # make ith element as 0
                if i != n - 1 and l[i + 1] == 1:  # quit if consecutive 1 occurs
                    break
        return result + 1 - is_consecutive
