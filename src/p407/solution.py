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
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        n = len(heightMap)
        m = 0 if n == 0 else len(heightMap[0])
        q = PriorityQueue()
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            visited[i][0] = 1
            visited[i][m - 1] = 1
            q.push((heightMap[i][0], i, 0))
            q.push((heightMap[i][m - 1], i, m - 1))
        for i in range(1, m - 1):
            visited[0][i] = 1
            visited[n - 1][i] = 1
            q.push((heightMap[0][i], 0, i))
            q.push((heightMap[n - 1][i], n - 1, i))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        result = 0
        while len(q) > 0:
            h, x, y = q.pop()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    result += max(0, h - heightMap[nx][ny])
                    q.push((max(heightMap[nx][ny], h), nx, ny))
        return result


Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
