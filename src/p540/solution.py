class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        import operator
        return functools.reduce(operator.xor, nums, 0)
