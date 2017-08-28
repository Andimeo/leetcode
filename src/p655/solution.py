class Solution:
    def DFS(self, root):
        if root is None:
            return 0
        return max(self.DFS(root.left), self.DFS(root.right)) + 1

    def DFS2(self, root, depth, left, right):
        if root is None:
            return
        pos = (left + right) >> 1
        # print(self.depth - depth, pos, root.val)
        self.result[self.depth - depth][pos] = str(root.val)
        self.DFS2(root.left, depth - 1, left, pos)
        self.DFS2(root.right, depth - 1, pos, right)

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.depth = self.DFS(root)
        self.result = [[""] * (2 ** self.depth - 1) for _ in range(self.depth)]
        self.DFS2(root, self.depth, 0, 2 ** self.depth - 1)
        return self.result
