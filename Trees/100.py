# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Base case 1: If both nodes are null, the trees are identical at this node
        if not p and not q:
            return True
        
        # Base case 2: If one node is null and the other is not, the trees are not identical
        if not p or not q:
            return False
        
        # Base case 3: If the values of the nodes are different, the trees are not identical
        if p.val != q.val:
            return False
            
        # Recursive step: 
        # Return True only if both the left subtrees and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
