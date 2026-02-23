# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# -----------------------------------
# BST Iterator using Controlled Inorder Traversal
# -----------------------------------
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        # Stack to simulate recursion
        self.stack = []

        # Push all left nodes starting from root
        self._push_left(root)


    # -----------------------------------
    # Helper function to push all left nodes
    # -----------------------------------
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left


    # -----------------------------------
    # Return next smallest element
    # -----------------------------------
    def next(self):
        """
        :rtype: int
        """
        # Top of stack is next smallest
        node = self.stack.pop()

        # If right child exists,
        # push all left nodes of right subtree
        if node.right:
            self._push_left(node.right)

        return node.val


    # -----------------------------------
    # Check if next element exists
    # -----------------------------------
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0