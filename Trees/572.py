# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
#         # Base case 1: If t is None, it is a subtree of s by definition
#         if not t:
#             return True
        
#         # Base case 2: If s is None but t is not, t can't be a subtree of s
#         if not s:
#             return False
        
#         # If trees rooted at s and t are the same, return True
#         if self.sameTree(s, t):
#             return True
        
#         # Otherwise, recursively check left and right subtrees of s
#         # to see if t is a subtree of either
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
#     def sameTree(self, s, t):
#         # Base case 1: If both nodes are None, trees are identical
#         if not s and not t:
#             return True
        
#         # If both nodes exist and their values are equal,
#         # recursively check their left and right subtrees
#         if s and t and s.val == t.val:
#             return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        
#         # In all other cases, trees are not identical
#         return False


#ORR

# def listTree(root):
#     # Base case: If the current node is None, represent it with '#'
#     if root is None:
#         return '#'
    
#     # Preorder traversal representation as a string:
#     # ',' + current node value + left subtree + right subtree
#     return ',' + str(root.val) + listTree(root.left) + listTree(root.right)

# # Serialize the entire tree into a string
# r = listTree(root)

# # Serialize the subtree into a string
# sr = listTree(subRoot)

# # Check if the serialized subtree string is a substring of the serialized main tree
# if sr in r:
#     return True

# # If not found, subtree is not part of main tree
# return False
