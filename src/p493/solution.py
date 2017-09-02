class Solution(object):
    def merge(self, nums, left, mid, right):
        result = 0
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= 2 * nums[j]:
                result += j - mid - 1
                i += 1
            else:
                j += 1
        while i <= mid:
            result += right - mid + 1
            i += 1
        i, j = left, mid + 1
        l = []
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                l.append(nums[i])
                i += 1
            else:
                l.append(nums[j])
                j += 1
        while i <= mid:
            l.append(nums[i])
            i += 1
        while j <= right:
            l.append(nums[j])
            j += 1
        assert len(l) == right - left + 1
        for i in range(len(l)):
            nums[i + left] = l[i]
        return result

    def mergesort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        result = 0
        result += self.mergesort(nums, left, mid)
        result += self.mergesort(nums, mid + 1, right)
        result += self.merge(nums, left, mid, right)
        return result

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergesort(nums, 0, len(nums) - 1)


