class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        ds = collections.defaultdict(int)
        dt = collections.defaultdict(int)
        has_found = 0
        for c in t:
            dt[c] += 1
        left = 0
        start, end = -1, len(s)
        for i, c in enumerate(s):
            if c in dt:
                ds[c] += 1
                if ds[c] <= dt[c]:
                    has_found += 1
                if has_found == len(t):
                    while s[left] not in dt or dt[s[left]] < ds[s[left]]:
                        if s[left] in dt:
                            ds[s[left]] -= 1
                        left += 1
                    if end - start > i - left:
                        start, end = left, i
                    ds[s[left]] -= 1
                    left += 1
                    has_found -= 1
        return "" if start == -1 else s[start:end + 1]
