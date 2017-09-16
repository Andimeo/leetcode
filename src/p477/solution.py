class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        n = len(nums)
        for num in nums:
            for i in range(32):
                if num & 1 == 1:
                    bits[i] += 1
                num >>= 1
        result = 0
        for bit in bits:
            result += bit * (n - bit)
        return result
