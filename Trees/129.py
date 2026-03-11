from collections import deque

# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------------
# Build tree from level-order list
# Example: [1,2,3,None,4]
# -----------------------------------
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # List to store all root-to-leaf numbers
        res = []

        # DFS function
        def dfs(node, num):

            # Base case
            if not node:
                return

            # Build current number
            newNum = num * 10 + node.val

            # If leaf node → store number
            if not node.left and not node.right:
                res.append(newNum)
                return

            # Recur left & right
            dfs(node.left, newNum)
            dfs(node.right, newNum)

        # Edge case
        if not root:
            return 0

        dfs(root, 0)

        # Return total sum
        return sum(res)


# ---- Test Setup ----
root_list = [1, 2, 3]
root = build_tree(root_list)

sol = Solution()
print("Answer:", sol.sumNumbers(root))