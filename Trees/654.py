'''
If the question says:

“next greater”

“previous smaller”

“nearest taller”

“first element to the right that…”

It means MONOTONIC STACK.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nums = [3, 2, 1, 6, 0, 5]

stack = []

for i in nums:
    node = TreeNode(i)
    last_popped = None

    while stack and node.val > stack[-1].val:
        last_popped = stack.pop()

    if last_popped:
        node.left = last_popped

    if stack:
        stack[-1].right = node

    stack.append(node)

root = stack[0]


# ---------------------------------------------------------
# EXPLANATION:
# This code constructs a MAXIMUM BINARY TREE from an array.
#
# Definition of Maximum Binary Tree:
# - The root is the maximum number in the array
# - The left subtree is the maximum tree of elements left of max
# - The right subtree is the maximum tree of elements right of max
#
# This implementation builds the tree in O(n) time
# using a MONOTONIC DECREASING STACK.
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY IDEA (MONOTONIC STACK):
#
# The stack always keeps nodes in DECREASING order of values.
#
# When a new value is GREATER than stack top:
# - It means this new value should be ABOVE those smaller values
# - So we pop smaller nodes and make them LEFT children
#
# If stack still has elements:
# - The current node becomes the RIGHT child of stack[-1]
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHAT EACH STEP DOES:
#
# 1) Create a TreeNode for current value
# 2) Pop all smaller values from stack
# 3) The last popped node becomes LEFT child
# 4) If stack is not empty, current node becomes RIGHT child
# 5) Push current node into stack
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [3, 2, 1, 6, 0, 5]
#
# -------------------------
# i = 3
# stack empty → push 3
# stack = [3]
#
# -------------------------
# i = 2
# 2 < 3 → no pop
# 3.right = 2
# stack = [3, 2]
#
# -------------------------
# i = 1
# 1 < 2 → no pop
# 2.right = 1
# stack = [3, 2, 1]
#
# -------------------------
# i = 6
# 6 > 1 → pop 1
# 6 > 2 → pop 2
# 6 > 3 → pop 3
# last_popped = 3
#
# 6.left = 3
# stack empty → no right assignment
# push 6
# stack = [6]
#
# -------------------------
# i = 0
# 0 < 6 → no pop
# 6.right = 0
# stack = [6, 0]
#
# -------------------------
# i = 5
# 5 > 0 → pop 0
# last_popped = 0
#
# 5 < 6 → stop popping
# 5.left = 0
# 6.right = 5
# stack = [6, 5]
#
# -------------------------
# ROOT:
# root = stack[0] = 6
# ---------------------------------------------------------

# ---------------------------------------------------------
# FINAL TREE STRUCTURE:
#
#          6
#        /   \
#       3     5
#        \   /
#         2 0
#          \
#           1
#
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) → each element pushed & popped once
#
# SPACE COMPLEXITY:
# O(n) → stack
# ---------------------------------------------------------
