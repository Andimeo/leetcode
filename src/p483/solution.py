class Solution(object):
    # https://discuss.leetcode.com/topic/82130/java-solution-with-hand-writing-explain
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        for l in range(62, 1, -1):
            low, high = 2, n
            while low <= high:
                mid = (low + high) >> 1
                if n * (mid - 1) == mid ** l - 1:
                    return str(mid)
                if n * (mid - 1) < mid ** l - 1:
                    high = mid - 1
                else:
                    low = mid + 1
        return None
