# -----------------------------------
# Definition for a binary tree node.
# -----------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------------
# BUILD TREE
# -----------------------------------
#        1
#       / \
#      2   3
#       \
#        5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)


# -----------------------------------
# PRINT TREE (LEVEL ORDER)
# -----------------------------------
from collections import deque

def print_tree(root):
    if not root:
        return
    
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            print(node.val, end=" ")
            q.append(node.left)
            q.append(node.right)
        else:
            print("None", end=" ")
    print()


print("Tree (level order):")
print_tree(root)


# -----------------------------------
# Solution Class
# -----------------------------------
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
        res = []   # Final result list
        
        # -----------------------------------
        # DFS Helper Function
        # -----------------------------------
        def dfs(node, inter_res):
            
            if not node:
                return
            
            # Add current node to path
            inter_res.append(str(node.val))
            
            # If leaf node → store path
            if not node.left and not node.right:
                res.append("->".join(inter_res))
            
            # Recur left and right
            dfs(node.left, inter_res)
            dfs(node.right, inter_res)
            
            # Backtracking step
            inter_res.pop()
        
        dfs(root, [])
        return res


# -----------------------------------
# CALL FUNCTION
# -----------------------------------
sol = Solution()
result = sol.binaryTreePaths(root)

print("Returned Result:")
print(result)