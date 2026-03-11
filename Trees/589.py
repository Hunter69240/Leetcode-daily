# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def preorder(root):
    if not root:
        return []

    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)

        for child in reversed(node.children):
            stack.append(child)

    return res


root = Node(1)

node3 = Node(3)
node2 = Node(2)
node4 = Node(4)

node5 = Node(5)
node6 = Node(6)

# assign children
root.children = [node3, node2, node4]
node3.children = [node5, node6]

a = preorder(root)
print(a)


# ---------------------------------------------------------
# EXPLANATION:
# This code performs an ITERATIVE PREORDER TRAVERSAL
# of an N-ARY TREE.
#
# Preorder traversal order:
#   ROOT → CHILDREN (left to right)
#
# We use a STACK to simulate recursion.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY `reversed(node.children)` IS IMPORTANT:
#
# Stack is LIFO (Last In, First Out).
#
# To process children from LEFT to RIGHT,
# we must PUSH them onto the stack from RIGHT to LEFT.
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
# push children in reverse → push 4, 2, 3
# stack = [4, 2, 3]
#
# -------------------------
# pop → 3
# res = [1, 3]
# push children in reverse → push 6, 5
# stack = [4, 2, 6, 5]
#
# -------------------------
# pop → 5
# res = [1, 3, 5]
#
# -------------------------
# pop → 6
# res = [1, 3, 5, 6]
#
# -------------------------
# pop → 2
# res = [1, 3, 5, 6, 2]
#
# -------------------------
# pop → 4
# res = [1, 3, 5, 6, 2, 4]
#
# FINAL RESULT:
# [1, 3, 5, 6, 2, 4]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) — each node visited once
#
# SPACE COMPLEXITY:
# O(n) — stack in worst case
# ---------------------------------------------------------
