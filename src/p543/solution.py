# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0

        def DFS(root):
            if root is None:
                return 0
            l = DFS(root.left)
            r = DFS(root.right)
            ll = 0 if root.left is None else root.left.l
            lr = 0 if root.right is None else root.right.l
            root.l = max(ll, lr) + 1
            return max(l, r, ll + lr)

        return DFS(root)
