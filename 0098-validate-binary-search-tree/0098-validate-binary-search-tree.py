# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        def validate(node, left, right):
            if node is None:
                return True
            if (left is not None and node.val <= left) or (right is not None and node.val >= right):
                return False
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        
        return validate(root, None, None)
            """
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Check if the list is strictly increasing
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True
        
    
        