class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        leftx = min([x[0] for x in rectangles])
        lefty = min([x[1] for x in rectangles])
        rightx = max([x[2] for x in rectangles])
        righty = max([x[3] for x in rectangles])
        area = sum([(x[2] - x[0]) * (x[3] - x[1]) for x in rectangles])
        import collections
        counter = collections.defaultdict(int)
        ok = True
        for r in rectangles:
            counter[(r[0], r[1])] += 1
            counter[(r[2], r[3])] += 1
            counter[(r[0], r[3])] += 1
            counter[(r[2], r[1])] += 1
        ok = ok and counter[leftx, lefty] == 1 and counter[leftx, righty] == 1 and counter[rightx, lefty] == 1 and \
             counter[rightx, righty] == 1
        if not ok:
            return ok
        del counter[leftx, lefty]
        del counter[leftx, righty]
        del counter[rightx, lefty]
        del counter[rightx, righty]
        two_or_four = 0
        for p in counter:
            if counter[p] == 2 or counter[p] == 4:
                two_or_four += 1
            if counter[p] not in (2, 4):
                ok = False
                break
        ok = ok and area == (righty - lefty) * (rightx - leftx)
        return ok
