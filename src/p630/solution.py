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


class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        q = PriorityQueue(key=lambda x: -x)
        courses.sort(key=lambda x: x[1])
        time = 0
        for course in courses:
            if time + course[0] <= course[1]:
                q.push(course[0])
                time += course[0]
            else:
                if len(q) != 0 and q.top() > course[0]:
                    time += course[0] - q.pushpop(course[0])
        return len(q)


if __name__ == '__main__':
    Solution().scheduleCourse(None)
