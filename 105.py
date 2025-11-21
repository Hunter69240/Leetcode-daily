# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        
        Reconstructs a binary tree from preorder and inorder traversal lists.
        """

        # Base case: if either list is empty, no tree can be built
        if not preorder or not inorder:
            return None
        
        # First element in preorder is always the root of the current subtree
        root = TreeNode(preorder[0])
        
        # Find the root's position in the inorder list
        # This divides inorder into left subtree elements and right subtree elements
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree
        # preorder[1:mid+1] → nodes in preorder that belong to the left subtree
        # inorder[:mid]     → nodes in inorder that belong to the left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Recursively build the right subtree
        # preorder[mid+1:]  → remaining nodes in preorder for the right subtree
        # inorder[mid+1:]   → nodes in inorder that belong to the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the constructed subtree root
        return root
