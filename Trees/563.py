# ============================================================
# ⭐ IMPORTANT IDEA (FOR MANY TREE PROBLEMS)
#
# IF A PROBLEM ASKS ABOUT SUBTREE VALUES / MOVES / BALANCE /
# OR SOMETHING THAT DEPENDS ON CHILDREN → THINK POSTORDER
#
# Reason:
# Postorder processes nodes in this order:
#        LEFT → RIGHT → ROOT
#
# So when we reach a node, we already know the result of
# its left and right subtree.
#
# That is why POSTORDER is commonly used for:
# • subtree sum
# • coin distribution
# • balance checking
# • tree DP problems
# ============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility: Print tree using inorder traversal
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)


# Solution
def solution(root):

    total_tile = 0   # stores total operations / moves

    def postorder(node):
        nonlocal total_tile

        if not node:
            return 0

        # Step 1: Solve left subtree
        left = postorder(node.left)

        # Step 2: Solve right subtree
        right = postorder(node.right)

        # Step 3: Calculate difference
        total_tile = total_tile + abs(left - right)

        # Step 4: Return subtree sum
        return left + right + node.val

    postorder(root)

    return total_tile


# Create Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


# Print Tree
print("Tree (Inorder):")
printTree(root)
print()


# Call Solution
print("Answer:", solution(root))


"""
DRY RUN
---------------------------------

Tree:
        4
      /   \
     2     6
    / \
   1   3


POSTORDER ORDER
----------------
1 → 3 → 2 → 6 → 4


Step 1
Node = 1
left = 0
right = 0
total_tile += |0-0| = 0
return 1


Step 2
Node = 3
left = 0
right = 0
total_tile += |0-0| = 0
return 3


Step 3
Node = 2
left = 1
right = 3
total_tile += |1-3| = 2
return 1 + 3 + 2 = 6


Step 4
Node = 6
left = 0
right = 0
total_tile += |0-0| = 0
return 6


Step 5
Node = 4
left = 6
right = 6
total_tile += |6-6| = 0
return 16


FINAL ANSWER
------------
total_tile = 2
"""


"""
TIME COMPLEXITY
---------------
O(N)
Each node is visited once.


SPACE COMPLEXITY
----------------
O(H)
H = height of tree (recursion stack)

Worst case → O(N)
Balanced tree → O(log N)
"""