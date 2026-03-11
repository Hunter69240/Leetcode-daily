# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility: Inorder traversal to print tree
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)


class Solution:
    def largestValues(self, root):

        # result list to store largest value of each level
        res = []

        # edge case
        if not root:
            return res

        # queue for BFS traversal
        queue = [root]

        # BFS traversal
        while queue:

            # store values of current level
            value_queue = []

            for i in range(len(queue)):

                node = queue.pop(0)

                # add current node value
                value_queue.append(node.val)

                # add children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # store maximum value of this level
            res.append(max(value_queue))

        return res


# ------------------------------
# Build Sample Tree
#
#        1
#       / \
#      3   2
#     / \   \
#    5   3   9
# ------------------------------

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)


# Print tree
print("Inorder Traversal:")
printTree(root)
print()


# Call solution
sol = Solution()
result = sol.largestValues(root)

print("Largest Value in Each Row:", result)