from collections import deque

# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Node value
        self.left = left      # Left child
        self.right = right    # Right child


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution(object):
    def hasPathSum(self, root, remaining):
        """
        Check if there exists a root-to-leaf path 
        such that adding all the values equals targetSum.

        :type root: Optional[TreeNode]
        :type remaining: int
        :rtype: bool
        """

        # Depth First Search (DFS)
        def dfs(node, remainingSum):

            # Base Case 1: If node is None → no path
            if not node:
                return False

            # Step 1: Subtract current node value
            remainingSum = remainingSum - node.val

            # Step 2: If leaf node AND remainingSum becomes 0
            # we found valid path
            if remainingSum == 0 and node.left is None and node.right is None:
                return True

            # Step 3: Recurse left OR right
            # If either subtree returns True → answer is True
            return dfs(node.left, remainingSum) or dfs(node.right, remainingSum)

        # Initial DFS call
        return dfs(root, remaining)



# -----------------------------------
# Helper Function: Level Order Print
# -----------------------------------
def print_tree_level_order(root):
    if not root:
        print("Tree is empty")
        return

    queue = deque([root])
    print("Level Order Traversal:")

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


# -----------------------------------
# Create Sample Tree
# -----------------------------------
def create_sample_tree():
    """
            5
           / \
          4   8
         /   / \
        11  13  4
       /  \
      7    2
    """

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    return root


# -----------------------------------
# Driver Code
# -----------------------------------
if __name__ == "__main__":

    root = create_sample_tree()
    target = 22

    print_tree_level_order(root)

    sol = Solution()
    result = sol.hasPathSum(root, target)

    print("Has Path Sum =", result)