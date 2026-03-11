# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # Base Case:
        # If inorder list is empty → no tree/subtree
        if not inorder:
            return None

        # Last element in postorder is the root
        root = TreeNode(postorder.pop())

        # Find index of root in inorder
        # This splits left and right subtree
        idx = inorder.index(root.val)

        # IMPORTANT:
        # Build RIGHT subtree first because
        # postorder pops elements from the end
        root.right = self.buildTree(inorder[idx+1:], postorder)

        # Then build LEFT subtree
        root.left = self.buildTree(inorder[:idx], postorder)

        return root