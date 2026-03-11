from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # If tree is empty, return empty list
        if not root:
            return []

        result = []                      # Final answer
        queue = deque([root])            # BFS queue
        left_to_right = True             # Direction flag

        # Process level by level
        while queue:

            level_size = len(queue)      # Number of nodes at current level
            level = deque()              # Use deque for zigzag insertion

            # Process all nodes of current level
            for _ in range(level_size):

                node = queue.popleft()   # Remove node from front

                # Insert based on direction
                if left_to_right:
                    level.append(node.val)       # Normal order
                else:
                    level.appendleft(node.val)   # Reverse order

                # Add children for next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Add current level to result
            result.append(list(level))

            # Flip direction for next level
            left_to_right = not left_to_right

        return result