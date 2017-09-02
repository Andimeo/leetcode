class IntervalTreeNode:
    def __init__(self, left=0, right=0, val=0, index=0):
        self.left = left
        self.right = right
        self.val = val
        self.index = index


class MaxIntervalTree:
    def __init__(self, values):
        self.values = values
        self.interval_tree = [None] * len(self.values) * 4
        # mapping between the pos in values and pos in interval_tree
        self.d = {}
        self._build(0, len(self.values) - 1, 0)

    def _build(self, left, right, node):
        self.interval_tree[node] = IntervalTreeNode(0, 0, 0)
        self.interval_tree[node].left = left
        self.interval_tree[node].right = right
        if left == right:
            self.interval_tree[node].val = self.values[left]
            self.interval_tree[node].index = left
            self.d[left] = node
            return
        mid = (left + right) >> 1
        self._build(left, mid, node * 2 + 1)
        self._build(mid + 1, right, node * 2 + 2)
        left_max = self.interval_tree[node * 2 + 1].val
        right_max = self.interval_tree[node * 2 + 2].val
        if left_max > right_max:
            self.interval_tree[node].val = left_max
            self.interval_tree[node].index = self.interval_tree[node * 2 + 1].index
        else:
            self.interval_tree[node].val = right_max
            self.interval_tree[node].index = self.interval_tree[node * 2 + 2].index

    def query(self, left, right):
        if left > right:
            return 0, -1
        return self._query(left, right, 0)

    def _query(self, left, right, node):
        if left <= self.interval_tree[node].left and right >= self.interval_tree[node].right:
            return self.interval_tree[node].val, self.interval_tree[node].index

        mid = (self.interval_tree[node].left + self.interval_tree[node].right) >> 1
        if right <= mid:
            return self._query(left, right, node * 2 + 1)
        if left > mid:
            return self._query(left, right, node * 2 + 2)

        left_max, left_index = self._query(left, mid, node * 2 + 1)
        right_max, right_index = self._query(mid + 1, right, node * 2 + 2)
        if left_max > right_max:
            return left_max, left_index
        else:
            return right_max, right_index

    def remove(self, pos):
        node = self.d[pos]
        self.interval_tree[node].val = 0
        while True:
            parent = (node - 1) // 2
            left_max = self.interval_tree[parent * 2 + 1].val
            right_max = self.interval_tree[parent * 2 + 2].val
            if left_max > right_max:
                self.interval_tree[parent].val = left_max
                self.interval_tree[parent].index = self.interval_tree[parent * 2 + 1].index
            else:
                self.interval_tree[parent].val = right_max
                self.interval_tree[parent].index = self.interval_tree[parent * 2 + 2].index
            node = parent
            if node == 0:
                break


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import collections
        Project = collections.namedtuple('Project', 'capital profit')
        projects = [Project(c, p) for p, c in zip(Profits, Capital)]
        projects.sort(key=lambda p: p.capital)
        Profits = [p.profit for p in projects]
        Capital = [p.capital for p in projects]

        tree = MaxIntervalTree(Profits)
        for i in range(k):
            import bisect
            pos = bisect.bisect(Capital, W)
            max_profit, index = tree.query(0, pos - 1)
            if max_profit == 0:
                break
            W += max_profit
            tree.remove(index)
        return W
