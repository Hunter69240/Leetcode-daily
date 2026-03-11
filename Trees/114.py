#2 solutuions exist for this problem, both are provided below.
#Solution 1
res = []

def preorder(node, res):
    if not node:
        return
    res.append(node)

    preorder(node.left, res)
    preorder(node.right, res)


for i in range(len(res)):
    if i + 1 < len(res):
        node = res[i]
        node.left = None
        node.right = res[i + 1]
    else:
        node = res[i]
        node.left = None
        node.right = None
    node = node.right


# ---------------------------------------------------------
# EXPLANATION:
# This code FLATTENS a binary tree into a linked list
# following PREORDER traversal order.
#
# Preorder order:
#   ROOT → LEFT → RIGHT
#
# The final structure:
# - All left pointers are set to None
# - All right pointers point to the next node in preorder
#
# This is exactly what the "Flatten Binary Tree to Linked List"
# problem asks for.
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 1: PREORDER TRAVERSAL
#
# preorder(node, res) traverses the tree and stores
# ACTUAL NODE REFERENCES (not values) into the list `res`
#
# Example tree:
#
#        1
#       / \
#      2   5
#     / \   \
#    3   4   6
#
# After preorder traversal:
# res = [1, 2, 3, 4, 5, 6]
#
# IMPORTANT:
# - res contains the ORIGINAL nodes
# - Modifying nodes in res modifies the original tree
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 2: RE-WIRE POINTERS
#
# We iterate through res and:
# - Set node.left = None
# - Set node.right = next node in preorder
#
# For each index i:
#
# i = 0:
#   node = res[0] → 1
#   node.left = None
#   node.right = res[1] → 2
#
# i = 1:
#   node = res[1] → 2
#   node.left = None
#   node.right = res[2] → 3
#
# i = 2:
#   node = res[2] → 3
#   node.left = None
#   node.right = res[3] → 4
#
# ...
#
# Last node:
#   node.right = None
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (FULL):
#
# res = [1, 2, 3, 4, 5, 6]
#
# After loop:
#
# 1 → right → 2 → right → 3 → right → 4 → right → 5 → right → 6 → None
#
# All left pointers are None.
#
# FINAL TREE (LINKED LIST):
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# ---------------------------------------------------------

# ---------------------------------------------------------
# IMPORTANT NOTE:
# - This approach uses O(n) extra space for `res`
# - It is easy to understand and debug
# - There is also an O(1) space solution using pointer manipulation
# ---------------------------------------------------------


#Solution 2
if not root:
    return

stk = [root]
prev = None

while stk:
    node = stk.pop()

    if prev:
        prev.right = node
        prev.left = None

    if node.right:
        stk.append(node.right)

    if node.left:
        stk.append(node.left)

    prev = node


# ---------------------------------------------------------
# EXPLANATION:
# This code FLATTENS a binary tree into a linked list
# following PREORDER traversal (ROOT → LEFT → RIGHT),
# using an ITERATIVE STACK approach.
#
# Final structure:
# - All left pointers = None
# - Each node.right points to the next preorder node
#
# This modifies the ORIGINAL tree in-place.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY A STACK IS USED:
# - Recursive preorder uses the call stack implicitly
# - Here, we simulate recursion using an explicit stack
#
# Stack ensures nodes are processed in preorder:
# - Push RIGHT child first
# - Push LEFT child next
# → LEFT is processed before RIGHT
# ---------------------------------------------------------

# ---------------------------------------------------------
# ROLE OF `prev`:
# - `prev` keeps track of the previously processed node
# - For each new node:
#     prev.right = current node
#     prev.left  = None
#
# This creates the linked-list structure.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN EXAMPLE:
#
# Tree:
#        1
#       / \
#      2   5
#     / \   \
#    3   4   6
#
# Initial:
# stk = [1]
# prev = None
#
# ---------------------------------------------------------
# Iteration 1:
# pop → node = 1
# prev is None → no linking
# push node.right (5)
# push node.left (2)
# stk = [5, 2]
# prev = 1
#
# ---------------------------------------------------------
# Iteration 2:
# pop → node = 2
# prev exists → link:
#   1.right = 2
#   1.left = None
# push node.right (4)
# push node.left (3)
# stk = [5, 4, 3]
# prev = 2
#
# ---------------------------------------------------------
# Iteration 3:
# pop → node = 3
# link:
#   2.right = 3
#   2.left = None
# stk = [5, 4]
# prev = 3
#
# ---------------------------------------------------------
# Iteration 4:
# pop → node = 4
# link:
#   3.right = 4
#   3.left = None
# stk = [5]
# prev = 4
#
# ---------------------------------------------------------
# Iteration 5:
# pop → node = 5
# link:
#   4.right = 5
#   4.left = None
# push node.right (6)
# stk = [6]
# prev = 5
#
# ---------------------------------------------------------
# Iteration 6:
# pop → node = 6
# link:
#   5.right = 6
#   5.left = None
# stk = []
# prev = 6
#
# ---------------------------------------------------------
# FINAL RESULT (FLATTENED TREE):
#
# 1 → 2 → 3 → 4 → 5 → 6 → None
#
# All left pointers are None.
# ---------------------------------------------------------

# ---------------------------------------------------------
# COMPLEXITY:
# Time:  O(n)  → each node visited once
# Space: O(n)  → stack in worst case (skewed tree)
# ---------------------------------------------------------
