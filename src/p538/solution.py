# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def DFS(root, num):
            if root is None:
                return
            root.sum = root.val
            if root.right is not None:
                DFS(root.right, num)
                root.sum += root.right.sum
            if root.left is not None:
                DFS(root.left, num + root.sum)
                root.sum += root.left.sum
            root.val += num + (0 if root.right is None else root.right.sum)

        DFS(root, 0)
        return root
