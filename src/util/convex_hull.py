import collections
import functools


def dist(self, other):
    v = other - self
    return v.x ** 2 + v.y ** 2


def subtract(self, other):
    return type(self)(self.x - other.x, self.y - other.y)


Point = collections.namedtuple('Point', 'x y')
Point.__sub__ = subtract
Point.dist = dist


class ConvexHull:
    def __init__(self, points):
        self.points = points
        assert len(self.points) > 2
        self.stack = None

    def graham_scan(self):
        p0 = self._left_bottom_point()
        points_sorted_by_polar = self.points[1:]
        points_sorted_by_polar.sort(key=functools.cmp_to_key(ConvexHull.comparator(p0)))
        stack = collections.deque()
        stack.append(p0)
        stack.append(points_sorted_by_polar[0])
        stack.append(points_sorted_by_polar[1])
        for i in range(2, len(points_sorted_by_polar)):
            p = points_sorted_by_polar[i]
            while len(stack) >= 2:
                v1 = stack[-1] - stack[-2]
                v2 = p - stack[-1]
                if ConvexHull.cross_product(v1, v2) <= 0:  # must include equal to here
                    stack.pop()
                else:
                    break
            stack.append(p)
        self.stack = stack

    def graham_scan_with_all_points_on_hull(self):
        p0 = self._left_bottom_point()
        points_sorted_by_polar = self.points[1:]
        points_sorted_by_polar.sort(key=functools.cmp_to_key(ConvexHull.comparator(p0)))

        # A special case is that in the largest radial angle, there may be several points lies on a line,
        # we need to reverse the order of these points. In the initial radial sorting, a tie is broke by closer
        # one comes first. But for the points in the largest radial angle, the closer one comes last.
        if ConvexHull.cross_product(points_sorted_by_polar[0] - p0, points_sorted_by_polar[-1] - p0) != 0:
            for i in range(len(points_sorted_by_polar) - 1, -1, -1):
                v1 = points_sorted_by_polar[i] - p0
                v2 = points_sorted_by_polar[i - 1] - p0
                if ConvexHull.cross_product(v1, v2) != 0:
                    break
                points_sorted_by_polar[i], points_sorted_by_polar[i - 1] = \
                    points_sorted_by_polar[i - 1], points_sorted_by_polar[i]
        stack = collections.deque()
        stack.append(p0)
        stack.append(points_sorted_by_polar[0])
        stack.append(points_sorted_by_polar[1])
        for i in range(2, len(points_sorted_by_polar)):
            p = points_sorted_by_polar[i]
            while len(stack) >= 2:
                v1 = stack[-1] - stack[-2]
                v2 = p - stack[-1]
                if ConvexHull.cross_product(v1, v2) < 0:  # ignore equal to 0 cases to include them
                    stack.pop()
                else:
                    break
            stack.append(p)
        self.stack = stack

    @property
    def convex_hull(self):
        self.graham_scan()
        return list(self.stack)

    @property
    def points_on_convex_hull(self):
        self.graham_scan_with_all_points_on_hull()
        return list(self.stack)

    def _left_bottom_point(self):
        index = 0
        for i in range(1, len(self.points)):
            if self.points[i].y < self.points[index].y:
                index = i
            elif self.points[i].y == self.points[index].y and self.points[i].x < self.points[index].x:
                index = i
        self.points[index], self.points[0] = self.points[0], self.points[index]
        return self.points[0]

    @staticmethod
    def comparator(p):
        def cmp(p1, p2):
            v1 = p1 - p
            v2 = p2 - p
            result = ConvexHull.cross_product(v2, v1)
            if result == 0:
                return p.dist(p1) - p.dist(p2)
            return result

        return cmp

    @staticmethod
    def cross_product(v1, v2):
        return v1.x * v2.y - v1.y * v2.x

    @staticmethod
    def is_clockwise(v1, v2):
        return ConvexHull.cross_product(v1, v2) > 0

    @staticmethod
    def is_counterclockwise(v1, v2):
        return ConvexHull.cross_product(v1, v2) < 0

    @staticmethod
    def is_collinear(v1, v2):
        return ConvexHull.cross_product(v1, v2) == 0
    
    @staticmethod
    def on_segment(point, p1, p2):
        v1 = p1 - point
        v2 = p2 - point
        return ConvexHull.cross_product(v1, v2) == 0 and \
               min(p1.x, p2.x) <= point.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= point.y <= max(p1.y, p2.y)


if __name__ == '__main__':

    def test(test_case):
        points = [Point(x, y) for x, y in test_case]
        hull = ConvexHull(points)
        result = hull.convex_hull
        print('convex hull for: ', test_case)
        for point in result:
            print(point)
        print('points on convex hull: ')
        for point in hull.points_on_convex_hull:
            print(point)


    test([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
    test([[1, 2], [2, 2], [4, 2]])
    test([[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [1, 1]])
