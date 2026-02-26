# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------------
# -------- Create Tree --------
#        3
#       / \
#      9   20
#         /  \
#        15   7
# -----------------------------------
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# -----------------------------------
# Function to Print Tree (Level Order)
# -----------------------------------
from collections import deque

def print_tree(root):
    if not root:
        return
    
    queue = deque([root])      # Initialize queue with root
    
    while queue:
        node = queue.popleft() # Remove front node
        print(node.val, end=" ")
        
        # Add left child if exists
        if node.left:
            queue.append(node.left)
            
        # Add right child if exists
        if node.right:
            queue.append(node.right)

    print()


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # -----------------------------------
        # DFS Helper Function
        # node   -> current node
        # isLeft -> True if this node is a left child
        # -----------------------------------
        def dfs(node, isLeft):
            
            # Base Case 1: If node is null
            if not node:
                return 0
            
            # Base Case 2:
            # If this node is a left child
            # AND it has no children (leaf node)
            if isLeft and not node.left and not node.right:
                return node.val
            
            # Recursively check left subtree
            left_sum = dfs(node.left, True)
            
            # Recursively check right subtree
            right_sum = dfs(node.right, False)
            
            # Return total sum
            return left_sum + right_sum
        
        # Root is NOT a left child
        return dfs(root, False)


# -----------------------------------
# Driver Code
# -----------------------------------
print("Tree (Level Order):")
print_tree(root)

sol = Solution()
result = sol.sumOfLeftLeaves(root)

print("Result:", result)