class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        import collections
        q = collections.deque()
        q.append((0, root))
        sum = []
        count = []
        while len(q) > 0:
            depth, node = q.popleft()
            if len(sum) <= depth:
                sum.append(0)
                count.append(0)
            sum[depth] += node.val
            count[depth] += 1
            if node.left is not None:
                q.append((depth + 1, node.left))
            if node.right is not None:
                q.append((depth + 1, node.right))

        return [x / y for x, y in zip(sum, count)]
