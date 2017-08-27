class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        import collections
        d = collections.defaultdict(int)

        result = 0
        for num in reversed(nums):
            depth = num // 100
            order = num // 10 % 10
            value = num % 10
            left_child_order = order * 2 - 1
            right_child_order = order * 2
            count = d[depth + 1, left_child_order] + d[depth + 1, right_child_order]
            d[depth, order] = 1 if count == 0 else count
            result += d[depth, order] * value
        return result
