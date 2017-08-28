class Solution:
    def DFS(self, root):
        if root is None:
            return "N"
        rep = "l(" + self.DFS(root.left) + ")_" + str(root.val) + "_r(" + self.DFS(root.right) + ")"
        # print(rep)
        if rep in self.s and rep not in self.output:
            self.result.append(root)
            self.output.add(rep)
        else:
            self.s.add(rep)
        return rep

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.s = set()
        self.output = set()
        self.result = []
        self.DFS(root)
        return self.result
