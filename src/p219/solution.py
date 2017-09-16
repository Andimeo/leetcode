class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not k:
            return False
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            if i >= k:
                s.remove(nums[i - k])
            s.add(nums[i])
        return False
