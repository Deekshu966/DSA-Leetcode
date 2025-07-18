# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # Base case: If the tree is empty or key is not found
        if not root:
            return None

        # If the key to delete is smaller than root, go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the key to delete is greater than root, go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # === Node found ===

            # Case 1: Node has only right child or no child
            if not root.left:
                return root.right

            # Case 2: Node has only left child
            elif not root.right:
                return root.left

            # Case 3: Node has two children
            # Find the inorder successor (smallest in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Replace the node's value with the inorder successor's value
            root.val = successor.val

            # Delete the inorder successor (which is now a duplicate)
            root.right = self.deleteNode(root.right, successor.val)

        # Return the (possibly updated) root node
        return root