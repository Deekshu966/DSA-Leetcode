# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.values = set()  # Use a set for O(1) lookups
        self.recover(root, 0)

    def recover(self, node, val):
        """ Recovers the tree using DFS """
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.recover(node.left, 2 * val + 1)  # Left child formula
        self.recover(node.right, 2 * val + 2)  # Right child formula

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values  # O(1) lookup using set
