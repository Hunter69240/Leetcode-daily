# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        Finds the maximum path sum in a binary tree.
        A path can start and end at any node, but must follow parent-child connections.
        """

        # Initialize result list with the root's value.
        # Using a list so we can update it inside the dfs function without making it global.
        res = [root.val]

        def dfs(root):
            """
            Depth-first search helper function.
            Returns the maximum path sum starting from the current node and going down.
            Also updates the global max path sum (res[0]).
            """
            if not root:
                return 0  # Base case: Null node contributes 0 to the path sum

            # Recursively find max path sum from left and right children
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If a path sum is negative, ignore it (take 0) — we only want positive contributions
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update the result with the maximum path sum passing through the current node
            # This considers the case where the path goes from left → current → right
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the maximum sum path starting from current node and extending to one side
            # (because in a parent path, you can only go down one branch)
            return root.val + max(leftMax, rightMax)

        dfs(root)  # Start DFS from root
        return res[0]  # Final maximum path sum found
