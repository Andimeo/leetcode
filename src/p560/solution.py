class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        import collections
        d = collections.defaultdict(int)
        d[0] = 1
        result = 0
        for i, num in enumerate(nums):
            s += num
            result += d[s - k]
            d[s] += 1
            # print(d)
        return result
