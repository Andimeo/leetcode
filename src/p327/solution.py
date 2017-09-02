class Solution(object):
    def merge(self, nums, left, mid, right):
        result = 0
        i, j = left, mid + 1
        lower_result, upper_result = 0, 0
        while i <= mid and j <= right:
            if nums[i] < nums[j] - self.upper:
                lower_result += j - mid - 1
                i += 1
            else:
                j += 1
        while i <= mid:
            lower_result += right - mid
            i += 1
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j] - self.lower:
                upper_result += j - mid - 1
                i += 1
            else:
                j += 1
        while i <= mid:
            upper_result += right - mid
            i += 1
        result = lower_result - upper_result
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

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = list(nums)
        for i in range(1, len(nums)):
            sums[i] += sums[i - 1]
        self.lower = lower
        self.upper = upper
        return self.mergesort([0] + sums, 0, len(sums))
