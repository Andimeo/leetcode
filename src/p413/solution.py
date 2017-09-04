class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        i = 1
        while i < len(A):
            diff = A[i] - A[i - 1]
            j = i
            while j < len(A) and A[j] - A[j - 1] == diff:
                j += 1

            if j - i + 1 >= 3:
                result += (j - i) * (j - i - 1) // 2
            i = j
        return result
