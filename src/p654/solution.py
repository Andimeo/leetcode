class Solution:
    def DFS(self, left, right):
        if left == right:
            return None
        # print(left, right, self.nums[left:right])
        node = TreeNode(0)
        node.val, pos = max((v, i) for i, v in enumerate(self.nums[left:right]))
        node.left = self.DFS(left, pos + left)
        node.right = self.DFS(left + pos + 1, right)
        return node

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.DFS(0, len(nums))
