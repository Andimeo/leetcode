# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        insert = True
        import bisect
        pos = bisect.bisect(self.intervals, (val, Interval(val, val)))
        if pos != len(self.intervals):
            interval = self.intervals[pos][1]
            if interval.start <= val <= interval.end:
                return
            if val == interval.start - 1:
                interval.start = val
                insert = False
            if val == interval.end + 1:
                interval.end = val
                insert = False
        if pos != 0:
            interval = self.intervals[pos - 1][1]
            if interval.start <= val <= interval.end:
                return
            if val == interval.start - 1:
                interval.start = val
                insert = False
            if val == interval.end + 1:
                interval.end = val
                insert = False
        if pos != len(self.intervals) and pos != 0:
            interval1, interval2 = self.intervals[pos - 1][1], self.intervals[pos][1]
            if interval1.end >= interval2.start:
                self.intervals = self.intervals[:pos - 1] + \
                                 [(interval2.end, Interval(interval1.start, interval2.end))] + \
                                 self.intervals[pos + 1:]
                return
        if insert:
            self.intervals = self.intervals[:pos] + [(val, Interval(val, val))] + self.intervals[pos:]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return [x[1] for x in self.intervals]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
