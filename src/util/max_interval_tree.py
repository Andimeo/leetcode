class IntervalTreeNode:
    def __init__(self, left=0, right=0, val=0):
        self.left = left
        self.right = right
        self.val = val


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
            self.d[left] = node
            return
        mid = (left + right) >> 1
        self._build(left, mid, node * 2 + 1)
        self._build(mid + 1, right, node * 2 + 2)
        self.interval_tree[node].val = max(self.interval_tree[node * 2 + 1].val, self.interval_tree[node * 2 + 2].val)

    def query(self, left, right):
        return self._query(left, right, 0)

    def _query(self, left, right, node):
        if left <= self.interval_tree[node].left and right >= self.interval_tree[node].right:
            return self.interval_tree[node].val

        mid = (self.interval_tree[node].left + self.interval_tree[node].right) >> 1
        if right <= mid:
            return self._query(left, right, node * 2 + 1)
        if left > mid:
            return self._query(left, right, node * 2 + 2)

        return max(self._query(left, mid, node * 2 + 1), self._query(mid + 1, right, node * 2 + 2))

    def remove(self, pos):
        node = self.d[pos]
        self.interval_tree[node].val = 0
        while node != 0:
            parent = (node - 1) // 2
            self.interval_tree[parent].val = max(self.interval_tree[parent * 2 + 1].val,
                                                 self.interval_tree[parent * 2 + 2].val)
            node = parent


if __name__ == '__main__':
    tree = MaxIntervalTree([1, 2, 3, 4, 5])
    assert tree.query(1, 4) == 5
    tree.remove(2)
    assert tree.query(0, 2) == 2
    assert tree.query(0, 1) == 2
    assert tree.query(0, 3) == 4
