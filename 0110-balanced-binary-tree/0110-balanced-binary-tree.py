# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1+max(left, right)
        self.balanced = True   
        check(root)
        return self.balanced
