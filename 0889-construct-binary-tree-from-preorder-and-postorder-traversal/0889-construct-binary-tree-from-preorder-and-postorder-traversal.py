# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(preorder,postorder,root):
            if not preorder and not postorder:
                return None
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root
            left_val = preorder[1]
            mid = postorder.index(left_val)+1  
            root.left = build(preorder[1:mid+1], postorder[:mid],root.left)
            root.right = build(preorder[mid+1:],postorder[mid:-1],root.right)
            return root 
        return build(preorder,postorder,None)