# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            # Count dashes to determine depth
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Read the number (node value)
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            # Create a new node
            node = TreeNode(value)

            # If depth matches stack size, it’s the left child of the last node
            if depth == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                # Pop until we find the correct parent
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node
            
            # Add new node to the stack
            stack.append(node)

        return stack[0]  # Root node
        