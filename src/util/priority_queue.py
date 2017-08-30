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

    def pushpop(self, val):
        result = self.pop()
        self.push(val)
        return result

    def __len__(self):
        return len(self.elements)