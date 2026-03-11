# -----------------------------------
# Definition for a binary tree node
# -----------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------------
# Utility Function: Print Tree
# (Level Order Traversal)
# -----------------------------------
from collections import deque

def printTree(root):
    if not root:
        print("Empty Tree")
        return
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    print(result)


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution:
    def findFrequentTreeSum(self, root):
        """
        Returns the subtree sum(s) that appear most frequently.
        """

        # Dictionary to store frequency of each subtree sum
        freq_map = {}

        # List to store final result
        result = []

        # Variable to track maximum frequency seen so far
        maxFreq = 0

        # -----------------------------------
        # DFS Function (Postorder Traversal)
        # -----------------------------------
        def dfs(node):
            nonlocal maxFreq

            # Base Case
            if not node:
                return 0

            # Step 1: Compute left subtree sum
            left_sum = dfs(node.left)

            # Step 2: Compute right subtree sum
            right_sum = dfs(node.right)

            # Step 3: Compute current subtree sum
            current_sum = node.val + left_sum + right_sum

            # Step 4: Update frequency map
            freq_map[current_sum] = freq_map.get(current_sum, 0) + 1

            # Step 5: Update maximum frequency
            maxFreq = max(maxFreq, freq_map[current_sum])

            return current_sum

        # Run DFS
        dfs(root)

        # Collect sums that have max frequency
        for subtree_sum, freq in freq_map.items():
            if freq == maxFreq:
                result.append(subtree_sum)

        return result


# -----------------------
# Create Sample Tree
# -----------------------

# Example Tree:
#        5
#       / \
#      2   -5

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)

# Print Tree
print("Tree (Level Order):")
printTree(root)

# -----------------------
# Call Solution Function
# -----------------------

sol = Solution()
result = sol.findFrequentTreeSum(root)
print("Most Frequent Subtree Sum:", result)