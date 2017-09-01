from collections import defaultdict


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        record = defaultdict(lambda: 0)
        result = 0
        for row in wall:
            for i in range(1, len(row)):
                row[i] = row[i] + row[i - 1]
                record[row[i - 1]] += 1
                if record[row[i - 1]] > result:
                    result = record[row[i - 1]]
        return len(wall) - result
