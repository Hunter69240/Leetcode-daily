# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def postorder(root):
    res = []
    if not root:
        return res

    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        for i in node.children:
            stack.append(i)

    return res[::-1]


root = Node(1)

node3 = Node(3)
node2 = Node(2)
node4 = Node(4)

node5 = Node(5)
node6 = Node(6)

# assign children
root.children = [node3, node2, node4]
node3.children = [node5, node6]

a = postorder(root)
print(a)


# ---------------------------------------------------------
# EXPLANATION:
# This code performs an ITERATIVE POSTORDER TRAVERSAL
# of an N-ARY TREE.
#
# Postorder traversal order:
#   CHILDREN → ROOT
#
# Instead of using recursion, we use a STACK and a trick:
# - Perform a modified preorder traversal
# - Reverse the result at the end
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY TRICK:
#
# Normal preorder:
#   ROOT → CHILDREN
#
# Modified traversal here:
#   ROOT → CHILDREN (left to right)
#
# After reversing:
#   CHILDREN (right to left) → ROOT
#
# For N-ary trees, this reversal gives correct POSTORDER.
# ---------------------------------------------------------

# ---------------------------------------------------------
# TREE STRUCTURE:
#
#            1
#        /   |   \
#       3    2    4
#     /   \
#    5     6
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Initial:
# stack = [1]
# res = []
#
# -------------------------
# pop → 1
# res = [1]
# push children → 3, 2, 4
# stack = [3, 2, 4]
#
# -------------------------
# pop → 4
# res = [1, 4]
#
# -------------------------
# pop → 2
# res = [1, 4, 2]
#
# -------------------------
# pop → 3
# res = [1, 4, 2, 3]
# push children → 5, 6
# stack = [5, 6]
#
# -------------------------
# pop → 6
# res = [1, 4, 2, 3, 6]
#
# -------------------------
# pop → 5
# res = [1, 4, 2, 3, 6, 5]
#
# Reverse result:
# [5, 6, 3, 2, 4, 1]
#
# FINAL RESULT:
# [5, 6, 3, 2, 4, 1]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) — each node visited once
#
# SPACE COMPLEXITY:
# O(n) — stack and result list
# ---------------------------------------------------------
