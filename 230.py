# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        n = 0          # Counter to track how many nodes have been visited in sorted order
        stack = []     # Stack to simulate recursion for inorder traversal
        cur = root     # Start traversal from the root node

        # Continue until we have no nodes left to process (both cur is None and stack is empty)
        while cur or stack:
            # Step 1: Go to the leftmost node
            # Keep pushing current nodes onto the stack while moving left
            while cur:
                stack.append(cur)
                cur = cur.left

            # Step 2: Process the leftmost node
            cur = stack.pop()   # Get the node on top of the stack
            n += 1              # Increment visited node count

            # Step 3: Check if this is the k-th visited node
            if n == k:
                return cur.val   # Found the k-th smallest value, return it

            # Step 4: Move to the right subtree to continue traversal
            cur = cur.right
