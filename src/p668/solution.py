class Solution:
    @staticmethod
    def traverse(m, n, target):
        x, y = m, 1
        count = 0
        while x >= 1 and y <= n:
            if target < x * y:
                x -= 1
            else:
                y += 1
                count += x
        return count

    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low, high = 1, m * n
        ans = -1
        while low <= high:
            mid = (low + high) >> 1
            count = Solution.traverse(m, n, mid)
            if count >= k:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
