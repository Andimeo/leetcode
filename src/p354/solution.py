class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        result = []
        for e in envelopes:
            low, high = 0, len(result)
            while low < high:
                mid = (low + high) >> 1
                if result[mid][1] >= e[1]:
                    high = mid
                else:
                    low = mid + 1
            if low == len(result):
                result.append(e)
            else:
                result[low] = e
        return len(result)
