class Solution:
    """
    Dynamic programming: for n, k: [n][k] = \sigma_{i = max(0, k-(n-1))}^min(k, max_inverse_num_pre)
    """

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp_a = [0] * (k + 1)
        sum_a = [0] * (k + 1)
        dp_a[0] = 1
        sum_a[0] = 1
        for i in range(2, n + 1):
            dp_b = [0] * (k + 1)
            sum_b = [0] * (k + 1)
            dp_b[0] = 1
            sum_b[0] = 1
            max_inverse_num = i * (i - 1) // 2
            for j in range(1, min(k + 1, max_inverse_num + 1)):
                max_inverse_num_pre = (i - 1) * (i - 2) // 2
                index = min(max_inverse_num_pre, j)
                if i <= j:
                    # when i is smaller than or equal to j, ignore the items before j - i since it's unable to
                    # generate from them
                    dp_b[j] = (sum_a[index] - sum_a[j - i] + mod) % mod
                else:
                    dp_b[j] = sum_a[index]
                sum_b[j] = (sum_b[j - 1] + dp_b[j]) % mod
            dp_a = dp_b
            sum_a = sum_b
        return dp_a[k]
