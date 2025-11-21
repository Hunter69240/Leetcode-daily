# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform DFS and check balance + calculate height
        def dfs(root):
            # Base case: If node is None, it's balanced with height 0
            if not root:
                return [True, 0]

            # Recursively check left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Check if both left and right subtrees are balanced, and
            # the difference in their heights is no more than 1
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            # Return [is_balanced, height_of_subtree]
            return [balanced, 1 + max(left[1], right[1])]

        # Only need the balanced status for the whole tree, so return dfs(root)[0]
        return dfs(root)[0]
