class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = [1]
        s = set(result)
        sign = 1
        for i in range(k, 0, -1):
            result.append(result[-1] + sign * i)
            sign *= -1
            s.add(result[-1])
        for i in range(1, n + 1):
            if i not in s:
                result.append(i)
        return result
