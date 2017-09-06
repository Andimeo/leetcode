class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        A, B = min(nums), max(nums)
        r = max(1, int((B - A - 1) / (len(nums) - 1)) + 1)  # bucket range
        n = int((B - A) / r) + 1  # bucket len
        buckets = [[-1, -1] for _ in range(n)]
        for num in nums:
            bucket_num = (num - A) // r
            bucket = buckets[bucket_num]
            bucket[0] = num if bucket[0] == -1 else min(bucket[0], num)
            bucket[1] = num if bucket[1] == -1 else max(bucket[1], num)

        last = None
        for i in range(len(buckets)):
            if buckets[i][0] != -1:
                last = i
                break
        result = 0
        for i in range(last + 1, len(buckets)):
            if buckets[i][0] == -1:
                continue
            result = max(result, buckets[i][0] - buckets[last][1])
            last = i
        return result

Solution().maximumGap([3, 6, 9, 1])