class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        d = set()
        result = set()
        for num in nums:
            a = num - k
            b = num + k
            if a in d:
                result.add((min(num, a), max(num, a)))
            if b in d:
                result.add((min(num, b), max(num, b)))
            d.add(num)
        return len(result)
