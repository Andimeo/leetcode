import heapq


class PriorityQueue:
    def __init__(self, key=lambda a: a):
        self.elements = []
        self.key = key

    def push(self, val):
        ele = (self.key(val), val)
        heapq.heappush(self.elements, ele)

    def top(self):
        return self.elements[0][1]

    def pop(self):
        _, val = heapq.heappop(self.elements)
        return val

    def remove(self, value):
        index = None
        for i in range(len(self.elements)):
            if self.elements[i][1] == value:
                index = i
                break
        if index is None:
            return
        lastelt = self.elements.pop()
        if index == len(self.elements):
            return
        self.elements[index] = lastelt
        heapq._siftup(self.elements, index)
        # https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
        heapq._siftdown(self.elements, 0, index)

    def pushpop(self, val):
        result = self.pop()
        self.push(val)
        return result

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return self.elements.__str__()


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        self.min_heap = PriorityQueue()
        self.max_heap = PriorityQueue(key=lambda x: -x)
        l = []
        for i, num in enumerate(nums):
            self.add_num(num)
            if i >= k - 1:
                l.append(self.get_median())
                self.remove_num(nums[i - k + 1])
        return l

    def get_median(self):
        if len(self.min_heap) == 0:
            return 0
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap.top() / 1.
        else:
            return (self.max_heap.top() + self.min_heap.top()) / 2.

    def add_num(self, num):
        if len(self.min_heap) == 0 or num < self.min_heap.top():
            self.max_heap.push(num)
        else:
            self.min_heap.push(num)
        if len(self.max_heap) > len(self.min_heap):
            self.min_heap.push(self.max_heap.pop())
        if len(self.min_heap) > len(self.max_heap) + 1:
            self.max_heap.push(self.min_heap.pop())

    def remove_num(self, num):
        if len(self.max_heap) > 0 and num <= self.max_heap.top():
            self.max_heap.remove(num)
        else:
            self.min_heap.remove(num)
        if len(self.max_heap) > len(self.min_heap):
            self.min_heap.push(self.max_heap.pop())
        if len(self.min_heap) > len(self.max_heap) + 1:
            self.max_heap.push(self.min_heap.pop())
