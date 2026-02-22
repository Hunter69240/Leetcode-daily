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
    def minDepth(self, root):
        """
        Find the minimum depth of a binary tree.

        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Step 1: If tree is empty, depth is 0
        if not root:
            return 0
        
        # Step 2: Initialize depth counter
        depth = 0

        # Step 3: Use BFS (Level Order Traversal)
        # Queue stores nodes level by level
        queue = deque([root])

        # Step 4: Traverse level by level
        while queue:

            # Increase depth at start of each level
            depth += 1

            # Number of nodes at current level
            size = len(queue)

            # Process all nodes of current level
            for i in range(size):
                node = queue.popleft()

                # Step 5: If leaf node found,
                # return current depth immediately
                if node.left is None and node.right is None:
                    return depth

                # Otherwise, add children to queue
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


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
            1
           / \
          2   3
         /
        4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    return root


# -----------------------------------
# Driver Code
# -----------------------------------
if __name__ == "__main__":

    root = create_sample_tree()

    print_tree_level_order(root)

    sol = Solution()
    result = sol.minDepth(root)

    print("Minimum Depth:", result)