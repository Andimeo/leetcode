class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        d = [collections.defaultdict(int) for _ in range(len(A))]
        result = 0
        for i in range(len(A)):
            for j in range(i):
                # At last we update the count of all "generalized" slices for T(i, d)
                # by adding the three parts together: the original value of T(i, d), which
                # is c1 here, the counts from T(j, d), which is c2 and lastly the 1 count of
                # the "two-element" slice (A[j], A[i]).
                diff = A[i] - A[j]
                result += d[j][diff]
                d[i][diff] = d[i][diff] + d[j][diff] + 1
        return result
