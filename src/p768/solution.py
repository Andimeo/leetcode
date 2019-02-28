import heapq
from functools import cmp_to_key


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
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        q = PriorityQueue(key=lambda a: a[0][0] * 1.0 / a[0][1])
        for i in range(0, len(A) - 1):
            q.push(((A[i], A[-1]), (i, len(A) - 1)))

        result = None
        for i in range(K):
            item = q.pop()
            up_index = item[1][0]
            down_index = item[1][1]
            if down_index > up_index + 1:
                newItem = ((A[up_index], A[down_index - 1]), (up_index, down_index - 1))
                q.push(newItem)
            result = [A[up_index], A[down_index]]
        return result
