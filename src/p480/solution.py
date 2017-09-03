class IntervalTreeNode:
    def __init__(self, left=0, right=0, count=0):
        self.left = left
        self.right = right
        self.count = count


class IntervalTree:
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
        self.interval_tree[node].count = 0
        if left == right:
            self.d[left] = node
            return
        mid = (left + right) >> 1
        self._build(left, mid, node * 2 + 1)
        self._build(mid + 1, right, node * 2 + 2)

    def add(self, pos):
        self._add(pos, 0)

    def _add(self, pos, node):
        self.interval_tree[node].count += 1
        if self.interval_tree[node].left == self.interval_tree[node].right:
            return
        mid = (self.interval_tree[node].left + self.interval_tree[node].right) >> 1
        if pos <= mid:
            self._add(pos, node * 2 + 1)
        else:
            self._add(pos, node * 2 + 2)

    def query(self, k):
        return self._query(k, 0)

    def _query(self, k, node):
        if self.interval_tree[node].left == self.interval_tree[node].right:
            assert k == 1
            return self.values[self.interval_tree[node].left]

        if self.interval_tree[node * 2 + 1].count >= k:
            return self._query(k, node * 2 + 1)
        else:
            return self._query(k - self.interval_tree[node * 2 + 1].count, node * 2 + 2)

    def remove(self, pos):
        node = self.d[pos]
        self.interval_tree[node].count -= 1
        while node != 0:
            parent = (node - 1) // 2
            self.interval_tree[parent].count = \
                self.interval_tree[parent * 2 + 1].count + self.interval_tree[parent * 2 + 2].count
            node = parent
            if node == 0:
                break


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        nums = [(x[0], i, x[1]) for i, x in enumerate(nums)]
        tree = IntervalTree([x[2] for x in nums])
        l = []
        nums = sorted(nums, key=lambda x: x[0])
        for i, num in enumerate(nums):
            tree.add(num[1])
            if i >= k - 1:
                result = 0
                if k % 2 == 0:
                    result += tree.query((k - 1) // 2 + 1)
                    result += tree.query(k // 2 + 1)
                    result /= 2.
                else:
                    result = tree.query(k // 2 + 1)
                    result /= 1.
                l.append(result)
                tree.remove(nums[i - k + 1][1])
        return l
