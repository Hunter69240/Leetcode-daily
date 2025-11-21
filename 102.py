# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]   # Root of the binary tree
        :rtype: List[List[int]]          # List of levels, each containing node values
        """

        res = []  # Final result list (stores each level as a list of values)

        # Use a deque for efficient pop from the left
        q = collections.deque()
        q.append(root)  # Start BFS by adding the root node

        # Continue until the queue is empty
        while q:
            qLen = len(q)   # Number of nodes in the current level
            level = []      # Temporary list to store this level's values

            # Process all nodes at the current level
            for i in range(qLen):
                node = q.popleft()  # Remove the leftmost node from queue

                if node:  # If the node is not None
                    level.append(node.val)      # Add its value to this level's list
                    q.append(node.left)         # Add left child to queue
                    q.append(node.right)        # Add right child to queue

            # Only add the level to result if it's not empty
            if level:
                res.append(level)

        return res  # Return the list of all levels
