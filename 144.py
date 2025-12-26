res = []

def preorder(node, res):
    if not node:
        return
    res.append(node.data)

    preorder(node.left, res)
    preorder(node.right, res)


# ---------------------------------------------------------
# EXPLANATION:
# This function performs a PREORDER TRAVERSAL of a binary tree.
#
# Preorder traversal order:
#   1) Visit ROOT
#   2) Visit LEFT subtree
#   3) Visit RIGHT subtree
#
# The traversal is implemented using RECURSION.
#
# Parameters:
# - node : current node in the binary tree
# - res  : list to store the traversal result
#
# Base case:
# - If node is None, simply return (stop recursion)
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN EXAMPLE:
#
# Consider the binary tree:
#
#        1
#       / \
#      2   3
#     / \
#    4   5
#
# Call: preorder(root, res)
#
# Step-by-step:
#
# preorder(1):
#   res = [1]
#   preorder(2)
#
# preorder(2):
#   res = [1, 2]
#   preorder(4)
#
# preorder(4):
#   res = [1, 2, 4]
#   preorder(None) → return
#   preorder(None) → return
#
# back to preorder(2):
#   preorder(5)
#
# preorder(5):
#   res = [1, 2, 4, 5]
#   preorder(None) → return
#   preorder(None) → return
#
# back to preorder(1):
#   preorder(3)
#
# preorder(3):
#   res = [1, 2, 4, 5, 3]
#   preorder(None) → return
#   preorder(None) → return
#
# FINAL RESULT:
# res = [1, 2, 4, 5, 3]
# ---------------------------------------------------------
