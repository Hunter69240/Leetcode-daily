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
# Solution Class (Implement here)
# -----------------------------------
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # Your DFS + backtracking logic here
        result = []
        
        def dfs(node, remaining, path):
            
            if not node:
                return 
            
            path.append(node.val)
            remaining-=node.val

            if remaining == 0 and not node.left and not node.right:
                result.append(path[:])
            
            if node.left:
                dfs(node.left,remaining,path)
            if node.right:
                dfs(node.right,remaining,path)

            path.pop()
            
            
        
        dfs(root, targetSum, [])
        return result


# -----------------------------------
# Helper Function: Level Order Print
# -----------------------------------
def print_tree_level_order(root):
    if not root:
        print("Tree is empty")
        return

    queue = deque([root])
    print("Level Order Traversal:")

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


# -----------------------------------
# Create Sample Tree
# -----------------------------------
def create_sample_tree():
    """
            5
           / \
          4   8
         /   / \
        11  13  4
       /  \    / \
      7    2  5   1
    """

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    return root


# -----------------------------------
# Driver Code
# -----------------------------------
if __name__ == "__main__":

    root = create_sample_tree()
    target = 22

    print_tree_level_order(root)

    sol = Solution()
    result = sol.pathSum(root, target)

    print("All Paths with Sum =", result)