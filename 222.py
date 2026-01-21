class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_height(root):
    if root == None:
        return 0

    # compute height of leftmost path
    def left_height(root):
        left_count = 0
        while root != None:
            left_count += 1
            root = root.left
        return left_count

    # compute height of rightmost path
    def right_height(root):
        right_count = 0
        while root != None:
            right_count += 1
            root = root.right
        return right_count

    l = left_height(root)
    r = right_height(root)

    # if heights are equal → perfect binary tree
    if l == r:
        return (2 ** l) - 1
    else:
        count = 1 + find_height(root.left) + find_height(root.right)

    return count


# Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

# Connect nodes
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

a = find_height(root)
print(a)


# ---------------------------------------------------------
# EXPLANATION:
# This code COUNTS the number of nodes in a COMPLETE BINARY TREE.
#
# A complete binary tree:
# - All levels are completely filled except possibly the last
# - Last level nodes are filled from left to right
#
# The algorithm is optimized and runs faster than O(n).
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY IDEA:
#
# For a subtree:
# - If left height == right height
#   → it is a PERFECT binary tree
#   → number of nodes = 2^height - 1
#
# Otherwise:
# - Recursively count nodes in left and right subtrees
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY THIS WORKS:
#
# In a complete binary tree:
# - If leftmost height equals rightmost height,
#   the tree is fully filled
# - We can compute the count directly without traversal
#
# This avoids visiting every node.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Tree:
#
#            1
#          /   \
#         2     3
#        / \   /
#       4   5 6
#
# find_height(root):
#
# left_height = 3 (1 → 2 → 4)
# right_height = 2 (1 → 3)
#
# l != r → recurse
#
# count =
#   1 (root)
# + find_height(2)
# + find_height(3)
#
# find_height(2):
# left_height = 2
# right_height = 2
# → perfect tree
# → nodes = 2^2 - 1 = 3
#
# find_height(3):
# left_height = 2
# right_height = 1
# → recurse
# → count = 1 + 1 + 0 = 2
#
# TOTAL:
# 1 + 3 + 2 = 6
# ---------------------------------------------------------

# ---------------------------------------------------------
# FINAL ANSWER:
# 6
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O((log n)^2)
#
# SPACE COMPLEXITY:
# O(log n) due to recursion stack
# ---------------------------------------------------------
