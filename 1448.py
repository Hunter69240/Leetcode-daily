# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode        # Root of the binary tree
        :rtype: int                 # Count of 'good' nodes
        """

        # Helper DFS function:
        # node   → current node we're visiting
        # maxVal → maximum value seen so far along the path from root to this node
        def dfs(node, maxVal):
            if not node:  # Base case: reached a null node
                return 0

            # A node is 'good' if its value is >= all values seen so far
            # (meaning it's >= maxVal)
            res = 1 if node.val >= maxVal else 0

            # Update maxVal to the max value along the current path
            maxVal = max(maxVal, node.val)

            # Recurse left and right, adding their counts
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res  # Return total 'good' nodes from this subtree

        # Start DFS from root, initial maxVal is root's value
        return dfs(root, root.val)
