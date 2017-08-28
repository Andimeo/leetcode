class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        result = s / k
        for i in range(k, len(nums)):
            s -= nums[i - k]
            s += nums[i]
            result = max(result, s / k)
        return result
