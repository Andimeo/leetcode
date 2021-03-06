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
        if self.elements:
            self.elements[index] = lastelt
            heapq._siftup(self.elements, index)

    def pushpop(self, val):
        result = self.pop()
        self.push(val)
        return result

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return self.elements.__str__()


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        vl = []
        for l, r, h in buildings:
            vl.append((l, -h))
            vl.append((r, h))

        def cmp(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            return a[0] - b[0]

        import functools
        vl.sort(key=functools.cmp_to_key(cmp))
        q = PriorityQueue(key=lambda x: -x)
        q.push(0)
        result = []
        prev = 0
        for i in range(len(vl)):
            if vl[i][1] < 0:
                q.push(-vl[i][1])
            else:
                q.remove(vl[i][1])
            cur = q.top()
            if cur != prev:
                result.append([vl[i][0], cur])
                prev = cur
        return result
