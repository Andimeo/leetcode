# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        l = []
        q = collections.deque()
        q.append(root)
        while len(q) != 0:
            node = q.popleft()
            l.append(None if node is None else node.val)
            if node is None:
                continue
            q.append(node.left)
            q.append(node.right)
        return str(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = [x.strip() for x in data[1:-1].split(',') if x.strip()]
        if not l:
            return None
        root = TreeNode(int(l[0]))
        q = collections.deque()
        q.append(root)
        pos = 1
        while len(q) != 0:
            node = q.popleft()
            if pos >= len(l) or l[pos] == 'None':
                node.left = None
            else:
                node.left = TreeNode(int(l[pos]))
                q.append(node.left)
            pos += 1
            if pos >= len(l) or l[pos] == 'None':
                node.right = None
            else:
                node.right = TreeNode(int(l[pos]))
                q.append(node.right)
            pos += 1
        return root


#Your Codec object will be instantiated and called as such:
# root = TreeNode(1)
# root.right = TreeNode(2)
# codec = Codec()
# data = codec.serialize(root)
# print(data)
# codec.deserialize(data)
