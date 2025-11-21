# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """

#         # Helper function to validate a subtree
#         # 'node'  → current node being checked
#         # 'left'  → the minimum allowed value for this node (exclusive)
#         # 'right' → the maximum allowed value for this node (exclusive)
#         def valid(node, left, right):
#             # An empty tree is always valid
#             if not node:
#                 return True

#             # If the current node's value does not lie strictly between the allowed range
#             # then it's not a valid BST
#             if not (node.val < right and node.val > left):
#                 return False

#             # Recursively check:
#             # 1. Left subtree: max allowed value becomes the current node's value
#             # 2. Right subtree: min allowed value becomes the current node's value
#             return (
#                 valid(node.left, left, node.val) and
#                 valid(node.right, node.val, right)
#             )

#         # Initially, the whole tree can have any value
#         return valid(root, float("-inf"), float("inf"))


# # Python program to check if a tree is BST using Inorder Traversal

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.left = None
#         self.right = None

# # Recursive Function for inorder traversal
# def inorder(root, prev):
#     if root is None:
#         return True

#     # Recursively check the left subtree
#     if not inorder(root.left, prev):
#         return False

#     # Check the current node value against the previous value
#     if prev[0] >= root.data:
#         return False

#     # Update the previous value to the current node's value
#     prev[0] = root.data

#     # Recursively check the right subtree
#     return inorder(root.right, prev)

# # Function to check if the tree is a valid BST
# def isBST(root):
#     prev = [float('-inf')]
#     return inorder(root, prev)

# if __name__ == "__main__":
  
#     # Create a sample binary tree
#     #     10
#     #    /  \
#     #   5    20
#     #        / \
#     #       9   25

#     root = Node(10)
#     root.left = Node(5)
#     root.right = Node(20)
#     root.right.left = Node(9)
#     root.right.right = Node(25)

#     if isBST(root):
#         print("True")
#     else:
#         print("False")

