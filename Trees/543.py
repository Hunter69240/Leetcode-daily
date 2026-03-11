# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize result to store the maximum diameter found
        self.res = 0

        def dfs(curr):
            # Base case: if the current node is None, its height is 0
            if not curr:
                return 0
            
            # Recursively compute the height of the left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update the diameter: longest path is left height + right height
            self.res = max(self.res, left + right)

            # Return height of current node = 1 + max(left, right)
            return 1 + max(left, right)

        # Start DFS traversal from the root
        dfs(root)

        # Return the maximum diameter found
        return self.res
