class Solution:
    def DFS(self, root, k):
        if root is None:
            return
        if k - root.val in self.s:
            self.result = True
            return
        self.s.add(root.val)
        self.DFS(root.left, k)
        if self.result:
            return
        self.DFS(root.right, k)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.s = set()
        self.result = False
        self.DFS(root, k)
        return self.result
