import heapq


class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        heap = []
        max_value = -10 ** 5
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        ans = None
        while True:
            min_node = heap[0]
            if ans is None or ans[1] - ans[0] > max_value - min_node[0]:
                ans = [min_node[0], max_value]
            if min_node[2] + 1 >= len(nums[min_node[1]]):
                break
            heapq.heappushpop(heap, (nums[min_node[1]][min_node[2] + 1], min_node[1], min_node[2] + 1))
            max_value = max(max_value, nums[min_node[1]][min_node[2] + 1])
        return ans
