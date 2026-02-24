# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Node value (0 or 1)
        self.left = left        # Left child
        self.right = right      # Right child


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        Problem:
        Each root-to-leaf path represents a binary number.
        We must return the sum of all those binary numbers (in decimal form).
        """

        # -------------------------------------------------
        # DFS Function
        # -------------------------------------------------
        def dfs(node, current):
            """
            node    → current node in recursion
            current → decimal value of binary formed so far
            """

            # -------------------------
            # Base Case
            # -------------------------
            # If node is None → return 0
            if not node:
                return 0

            # -------------------------
            # Build Binary Number
            # -------------------------
            # Shift left by 1 (multiply by 2)
            # OR with node.val (add new bit)
            #
            # Example:
            # current = 3 (binary 11)
            # node.val = 0
            # (3 << 1) = 6  (110)
            # 6 | 0 = 6
            #
            current = (current << 1) | node.val

            # -------------------------
            # If Leaf Node
            # -------------------------
            # Leaf means no left and no right child
            if not node.left and not node.right:
                # Return the decimal value of this binary path
                return current

            # -------------------------
            # Recursive Calls
            # -------------------------
            # Return sum of left subtree and right subtree
            return dfs(node.left, current) + dfs(node.right, current)

        # Start DFS from root with initial value 0
        return dfs(root, 0)


# -------------------------------------------------
# Helper Function 1: Create Tree
# -------------------------------------------------
def create_tree():
    """
    Creates the following tree:

            1
          /   \
         0     1
        / \   / \
       0   1 0   1

    Root-to-leaf paths:
    100 → 4
    101 → 5
    110 → 6
    111 → 7

    Total = 4 + 5 + 6 + 7 = 22
    """

    root = TreeNode(1)

    root.left = TreeNode(0)
    root.right = TreeNode(1)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    return root


# -------------------------------------------------
# Helper Function 2: Level Order Print
# -------------------------------------------------
def print_tree(root):
    """
    Prints tree in level order (BFS traversal)
    """

    if not root:
        return

    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print()


# -------------------------------------------------
# Main Driver Code
# -------------------------------------------------
if __name__ == "__main__":

    # Create tree
    root = create_tree()

    print("Tree (Level Order):")
    print_tree(root)

    # Solve problem
    sol = Solution()
    result = sol.sumRootToLeaf(root)

    print("Result from sumRootToLeaf:", result)


"""
-------------------------------------
Time Complexity:
-------------------------------------
O(N)
Every node is visited once.

-------------------------------------
Space Complexity:
-------------------------------------
O(H)
H = height of tree (recursion stack)

Worst case (skewed tree) → O(N)
Balanced tree → O(log N)

-------------------------------------
Key Trick:
-------------------------------------
current = (current << 1) | node.val

This is same as:
current = current * 2 + node.val

Left shift builds binary efficiently.
"""