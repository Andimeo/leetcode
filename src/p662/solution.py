class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import collections
        q = collections.deque()
        q.append((1, 0, root))
        counter = collections.defaultdict(list)
        while len(q) != 0:
            depth, order, node = q.popleft()
            counter[depth].append(order)
            if node.left is not None:
                q.append((depth + 1, order * 2 + 1, node.left))
            if node.right is not None:
                q.append((depth + 1, order * 2 + 2, node.right))
        return max((max(depth) - min(depth) + 1 for depth in counter.values()))
