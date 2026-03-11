# ============================================================
# ⭐ IMPORTANT IDEA (REMEMBER FOR MANY BST PROBLEMS)
#
# IF GIVEN TREE IS A BST → THINK INORDER TRAVERSAL
#
# Reason:
# Inorder traversal of a BST always gives values in SORTED ORDER.
#
# Example:
# BST:
#        4
#      /   \
#     2     6
#    / \
#   1   3
#
# Inorder → 1 2 3 4 6
#
# Since values are sorted, the MINIMUM DIFFERENCE will always be
# between two ADJACENT elements in this inorder sequence.
#
# So while doing inorder traversal we compare:
# current_node_value - previous_node_value
# ============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility: Print tree in inorder (BST → sorted order)
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)


def getMinimumDifference(root):
    prev = None                 # stores previous visited node value
    min_diff = float("inf")     # stores minimum difference

    def inorder(node):
        nonlocal prev, min_diff

        if not node:
            return

        # Step 1: Traverse left subtree
        inorder(node.left)

        # Step 2: Process current node
        if prev is not None:
            diff = node.val - prev
            min_diff = min(min_diff, diff)

        # Update prev to current value
        prev = node.val

        # Step 3: Traverse right subtree
        inorder(node.right)

    inorder(root)
    return min_diff


# Constructing BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


# Print inorder traversal
printTree(root)
print()

# Find minimum difference
print(getMinimumDifference(root))


"""
DRY RUN
---------------------------------

BST:
        4
      /   \
     2     6
    / \
   1   3

Inorder Traversal → 1 2 3 4 6

Step-by-step:

prev = None
min_diff = ∞

Visit 1
prev = 1

Visit 2
diff = 2 - 1 = 1
min_diff = 1
prev = 2

Visit 3
diff = 3 - 2 = 1
min_diff = 1
prev = 3

Visit 4
diff = 4 - 3 = 1
min_diff = 1
prev = 4

Visit 6
diff = 6 - 4 = 2
min_diff = 1

Final Answer = 1
"""


"""
TIME COMPLEXITY
---------------
O(N)
We visit each node exactly once.


SPACE COMPLEXITY
----------------
O(H)
H = height of tree (recursion stack)

Worst case (skewed tree) → O(N)
Balanced BST → O(log N)
"""