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
        post_idx = {val: i for i, val in enumerate(postorder)}  # Create a hashmap for postorder indices

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            
            root = TreeNode(preorder[pre_start])  # Create root node
            
            if pre_start == pre_end:
                return root

            left_child_val = preorder[pre_start + 1]
            left_child_idx = post_idx[left_child_val]  # Find index of left child in postorder
            left_size = left_child_idx - post_start + 1  # Size of the left subtree

            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, post_start, left_child_idx)
            root.right = build(pre_start + left_size + 1, pre_end, left_child_idx + 1, post_end - 1)

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)