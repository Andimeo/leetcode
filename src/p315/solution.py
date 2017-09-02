class Solution(object):
    def merge(self, nums, left, mid, right):
        i, j = left, mid + 1
        l = []
        while i <= mid and j <= right:
            if nums[i][1] <= nums[j][1]:
                l.append(nums[i])
                self.result[nums[i][0]] += j - mid - 1
                i += 1
            else:
                l.append(nums[j])
                j += 1
        while i <= mid:
            l.append(nums[i])
            self.result[nums[i][0]] += right - mid
            i += 1
        while j <= right:
            l.append(nums[j])
            j += 1
        assert len(l) == right - left + 1
        for i in range(len(l)):
            nums[i + left] = l[i]

    def mergesort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.result = [0] * len(nums)
        self.mergesort(list(enumerate(nums)), 0, len(nums) - 1)
        return self.result


