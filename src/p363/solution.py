import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        # this is mandatory for test cases which has a larger row number than column number
        M, N = max(m, n), min(m, n)
        result = None
        for i in range(N):
            sums = [0] * M
            for j in range(i, N):
                num, l = 0, []
                for K in range(M):
                    sums[K] += matrix[j][K] if m < n else matrix[K][j]
                    num += sums[K]
                    if num <= k:
                        result = num if result is None else max(result, num)
                    pos = bisect.bisect_left(l, num - k)
                    if pos != len(l):
                        result = num - l[pos] if result is None else max(result, num - l[pos])
                    bisect.insort(l, num)
        return result
