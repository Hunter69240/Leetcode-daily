# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]   # Root of the binary tree
        :rtype: List[int]                # List of visible nodes from the right side
        """

        res = []  # Final result list: stores the rightmost node value from each level

        # Start BFS queue with the root node
        q = collections.deque([root])

        # Continue until all levels are processed
        while q:
            rightSide = None    # Will store the rightmost node of the current level
            qLen = len(q)       # Number of nodes at the current level

            # Process all nodes in this level
            for i in range(qLen):
                node = q.popleft()  # Get the next node in the queue

                if node:
                    # Keep overwriting rightSide as we move through the level
                    rightSide = node

                    # Add children to queue for the next level
                    q.append(node.left)
                    q.append(node.right)

            # After processing the level, rightSide will hold the last (rightmost) node
            if rightSide:
                res.append(rightSide.val)

        return res  # Return the list of rightmost nodes
