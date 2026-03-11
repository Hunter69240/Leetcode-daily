res = []

def postorder(node, res):
    if not node:
        return
    
    postorder(node.left, res)
    postorder(node.right, res)
    res.append(node.data)


# ---------------------------------------------------------
# EXPLANATION:
# This function performs a POSTORDER TRAVERSAL of a binary tree.
#
# Postorder traversal order:
#   1) Visit LEFT subtree
#   2) Visit RIGHT subtree
#   3) Visit ROOT
#
# The traversal is implemented using RECURSION.
#
# Parameters:
# - node : current node in the binary tree
# - res  : list to store the traversal result
#
# Base case:
# - If node is None, return immediately
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
# Call: postorder(root, res)
#
# Step-by-step:
#
# postorder(1):
#   postorder(2)
#
# postorder(2):
#   postorder(4)
#
# postorder(4):
#   postorder(None) → return
#   postorder(None) → return
#   append 4
#   res = [4]
#
# back to postorder(2):
#   postorder(5)
#
# postorder(5):
#   postorder(None) → return
#   postorder(None) → return
#   append 5
#   res = [4, 5]
#
# back to postorder(2):
#   append 2
#   res = [4, 5, 2]
#
# back to postorder(1):
#   postorder(3)
#
# postorder(3):
#   postorder(None) → return
#   postorder(None) → return
#   append 3
#   res = [4, 5, 2, 3]
#
# back to postorder(1):
#   append 1
#   res = [4, 5, 2, 3, 1]
#
# FINAL RESULT:
# res = [4, 5, 2, 3, 1]
# ---------------------------------------------------------
