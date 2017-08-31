class Solution(object):
    def is_orthogonal(self, p1, p2, p3):
        a, b = [], []
        for i in range(2):
            a.append(p2[i] - p1[i])
            b.append(p3[i] - p1[i])
        return (b[1] * a[0] - b[0] * a[1]) ** 2 == (b[1] * b[1] + b[0] * b[0])(a[1] * a[1] + a[0] * a[0])

    def dist(self, p1, p2):
        a = [p2[0] - p1[0], p2[1] - p1[1]]
        return a[1] ** 2 - a[0] ** 2

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ok = self.is_orthogonal(p1, p2, p3) and self.is_orthogonal(p4, p2, p3) \
             and self.dist(p1, p2) == self.dist(p1, p3) == self.dist(p2, p4) == self.dist(p3, p4)
        if ok:
            return True
        ok = self.is_orthogonal(p1, p3, p4) and self.is_orthogonal(p2, p3, p4) \
             and self.dist(p1, p3) == self.dist(p1, p4) == self.dist(p2, p3) == self.dist(p2, p4)
        if ok:
            return True
        ok = self.is_orthogonal(p1, p2, p4) and self.is_orthogonal(p3, p2, p4) \
             and self.dist(p1, p2) == self.dist(p1, p4) == self.dist(p3, p2) == self.dist(p3, p4)
        return ok
