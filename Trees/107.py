from collections import deque
def levelorder(self,root):
    from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # If tree is empty → return empty list
        if not root:
            return []

        queue = deque([root])   # BFS queue
        res = []                # Final result (top → bottom first)

        # Standard Level Order Traversal (BFS)
        while queue:

            level_size = len(queue)   # Number of nodes at current level
            sub_res = []              # Store values of current level

            for i in range(level_size):

                node = queue.popleft()   # Remove node from queue

                # Add children to queue for next level
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

                # Store current node value
                sub_res.append(node.val)

            # Add this level result
            res.append(sub_res)

        # Reverse the result to get bottom-up order
        return res[::-1]
