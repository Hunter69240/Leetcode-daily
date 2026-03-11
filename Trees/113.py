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
    def pathSum(self, root, targetSum):
        """
        Return all root-to-leaf paths where
        sum of node values equals targetSum.

        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        # This will store all valid paths
        result = []

        # DFS + Backtracking
        def dfs(node, remaining, path):

            # Base Case: If node is None, stop
            if not node:
                return

            # Step 1: Add current node to path
            path.append(node.val)

            # Step 2: Subtract node value from remaining sum
            remaining -= node.val

            # Step 3: If leaf node AND remaining becomes 0
            # we found a valid path
            if remaining == 0 and not node.left and not node.right:
                result.append(path[:])   # Make a copy of path

            # Step 4: Recurse left and right
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            # Step 5: Backtrack
            # Remove current node before returning
            path.pop()

        # Initial DFS call
        dfs(root, targetSum, [])

        return result


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
       /  \    / \
      7    2  5   1
    """

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    return root


# -----------------------------------
# Driver Code
# -----------------------------------
if __name__ == "__main__":

    root = create_sample_tree()
    target = 22

    print_tree_level_order(root)

    sol = Solution()
    result = sol.pathSum(root, target)

    print("All Paths with Sum =", result)