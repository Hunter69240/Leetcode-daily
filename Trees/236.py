# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Node value
        self.left = left        # Left child
        self.right = right      # Right child


# -----------------------------------
# Helper Function 1: Create Tree
# -----------------------------------
def create_tree():
    """
    Creates the following tree:

            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4

    Example:
    LCA(5, 1) = 3
    """

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    return root


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Problem:
        Find Lowest Common Ancestor (LCA) of nodes p and q.

        LCA Definition:
        The lowest node in the tree that has both p and q
        as descendants (a node can be descendant of itself).
        """

        # -------------------------
        # Base Case
        # -------------------------

        # If root is None → return None
        if not root:
            return None

        # If current node matches p or q
        # Then this node could be LCA
        if root == p or root == q:
            return root

        # -------------------------
        # Recursive Search
        # -------------------------

        # Search in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # -------------------------
        # Decision Making
        # -------------------------

        # Case 1:
        # If both left and right are NOT None
        # → p found in one subtree
        # → q found in other subtree
        # → Current node is LCA
        if left and right:
            return root

        # Case 2:
        # If only one side returned non-null
        # → Either LCA is deeper in subtree
        # → Or one of p/q itself is returned
        return left if left else right


# -----------------------------------
# Helper Function 2: Print Tree
# -----------------------------------
def print_tree(root):
    """
    Prints tree level by level (BFS)
    """

    if not root:
        return

    from collections import deque
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()


# -----------------------------------
# Driver Code
# -----------------------------------
if __name__ == "__main__":

    # Create tree
    root = create_tree()

    print("Tree (Level Order):")
    print_tree(root)

    sol = Solution()

    # Example 1: LCA of 5 and 1
    p = root.left        # Node 5
    q = root.right       # Node 1

    lca = sol.lowestCommonAncestor(root, p, q)

    print("\nLCA of", p.val, "and", q.val, "is:", lca.val)


"""
-------------------------------------
Dry Run for LCA(5, 1)
-------------------------------------

Call LCA(3, 5, 1)

At node 3:
    left  = search in subtree rooted at 5
    right = search in subtree rooted at 1

At node 5:
    root == p → return 5

At node 1:
    root == q → return 1

Back at node 3:
    left = 5
    right = 1
    Both non-null → return 3

Answer = 3

-------------------------------------
Time Complexity:
-------------------------------------
O(N)
Each node visited once.

-------------------------------------
Space Complexity:
-------------------------------------
O(H)
H = height of tree (recursion stack)

Worst case (skewed tree) → O(N)
Balanced tree → O(log N)
"""