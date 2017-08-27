class Solution:
    @staticmethod
    def is_increasing(nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, num in enumerate(nums[:-1]):
            if num > nums[i + 1]:
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                    return Solution.is_increasing(nums[i + 1:])
                if i == len(nums) - 2 or nums[i + 2] >= nums[i]:
                    return Solution.is_increasing(nums[i + 2:])
                return False
        return True
