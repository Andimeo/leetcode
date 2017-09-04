class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high = 0, sum(nums)
        result = None
        while low <= high:
            mid = (low + high) >> 1
            count = 0
            part_sum = 0
            i = 0
            while i < len(nums):
                if nums[i] > mid:
                    low = mid + 1
                    break
                if part_sum + nums[i] > mid:
                    count += 1
                    part_sum = 0
                else:
                    part_sum += nums[i]
                    i += 1
            else:
                if part_sum != 0:
                    count += 1
                if count <= m:
                    result = mid
                    high = mid - 1
                else:
                    low = mid + 1
        return result
