class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        q = collections.deque()
        l = []
        for i, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)
            if i > k - 1 and nums[i - k] == q[0]:
                q.popleft()
            if i >= k - 1:
                l.append(q[0])
        return l
