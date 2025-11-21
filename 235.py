# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode   # root of the Binary Search Tree
        :type p: TreeNode      # first target node
        :type q: TreeNode      # second target node
        :rtype: TreeNode       # returns the LCA node
        """

        # Start with the root node as the current node
        cur = root

        # Loop until we find the LCA (loop runs while there’s a current node)
        while cur:
            # Case 1: Both p and q are greater than the current node
            # This means LCA must be in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # Case 2: Both p and q are less than the current node
            # This means LCA must be in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # Case 3: p and q are on different sides 
            # OR one of them is equal to the current node
            # This means the current node is the split point → LCA found
            else:
                return cur
