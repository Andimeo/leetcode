class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        l = [int(x.split(':')[0]) * 60 + int(x.split(':')[1]) for x in timePoints]
        l.sort()
        r = [abs((l[i] - l[i - 1] + 1440) % 1440) for i in range(len(l))]
        return min(r)
