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
    def findBottomLeftValue(self, root):

        # queue for BFS traversal
        queue = []

        # result to store bottom left value
        res = 0

        # start with root node
        queue.append(root)

        # BFS traversal
        while queue:

            # iterate through current level
            for i in range(len(queue)):

                node = queue.pop(0)

                # add children to queue
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                # first node of every level is the leftmost
                if i == 0:
                    res = node.val

        return res


# ------------------------------
# Build Sample Tree
#
#        1
#       / \
#      2   3
#         / \
#        4   5
# ------------------------------

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


# Print tree
print("Inorder Traversal:")
printTree(root)
print()


# Call solution
sol = Solution()
result = sol.findBottomLeftValue(root)

print("Bottom Left Value:", result)