class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        s = (n + 1) * n // 2
        ss = nums[0]
        result = []
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                result.append(nums[i])
            else:
                ss += nums[i]
        result.append(s - ss)
        return result
