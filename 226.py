# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is None, return None
        if not root:
            return None
        
        # Swap the left and right children of the current node
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root node (now with left and right subtrees swapped)
        return root
