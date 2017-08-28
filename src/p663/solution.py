# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, root):
        if root is None:
            return 0
        sub_sum = self.DFS(root.left) + self.DFS(root.right) + root.val
        self.s[sub_sum] += 1
        return sub_sum

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import collections
        self.s = collections.defaultdict(int)
        sum = self.DFS(root)
        self.s[sum] -= 1  # We want to find the node which is not the root and has a sub_sum of sum // 2
        if sum % 2 == 1 or self.s[sum // 2] < 1:
            return False
        return True
