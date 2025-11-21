# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """
#         Encodes a tree into a single string using pre-order DFS.
#         Null nodes are represented by "N".
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []  # List to store traversal results as strings

#         def dfs(node):
#             # If the node is None, append "N" and stop
#             if not node:
#                 res.append("N")
#                 return 
#             # Append the current node's value
#             res.append(str(node.val))
#             # Recursively encode the left and right children
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         # Join all values into a single comma-separated string
#         return ",".join(res)

#     def deserialize(self, data):
#         """
#         Decodes a serialized string back into a binary tree.
#         Uses the same DFS pre-order structure from serialization.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         vals = data.split(",")  # Convert string back to list
#         self.i = 0  # Pointer to track the current position in vals

#         def dfs():
#             # If current value is "N", it represents a null node
#             if vals[self.i] == "N":
#                 self.i += 1
#                 return None
#             # Create a node from the current value
#             node = TreeNode(int(vals[self.i]))
#             self.i += 1
#             # Recursively build left and right subtrees
#             node.left = dfs()
#             node.right = dfs()
#             return node

#         return dfs()

# # Usage example:
# # ser = Codec()
# # deser = Codec()
# # serialized_tree = ser.serialize(root)     # Convert tree → string
# # deserialized_tree = deser.deserialize(serialized_tree)  # Convert string → tree


# Special BST Codec: Works only for Binary Search Trees
# Uses preorder traversal for serialization and BST property for reconstruction.

# TreeNode definition (LeetCode-style)
# class TreeNode(object):
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """
        Encodes a BST to a single string using preorder traversal.
        Preorder = root -> left -> right
        No "None" markers needed because BST structure can be recovered.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []  # Stores node values as strings

        def preorder(node):
            if node:
                # Add current node value
                res.append(str(node.val))
                # Recurse left then right
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        # Join values into a space-separated string
        return " ".join(res)

    def deserialize(self, data):
        """
        Decodes a string back into a BST.
        Uses preorder sequence + BST property to rebuild.
        
        :type data: str
        :rtype: TreeNode
        """
        # Convert string into list of integers (node values)
        pre = [int(x) for x in data.split()]

        def bstFromPreorder(pre):
            # Base case: if no values, return None
            if not pre:
                return None

            # First element is the root value (preorder property)
            root_val = pre[0]

            # Find first index where value is greater than root_val
            # This is where the right subtree begins
            i = 1
            while i < len(pre) and pre[i] < root_val:
                i += 1

            # Recursively build left and right subtrees
            # Left subtree: all values < root_val
            left_subtree = bstFromPreorder(pre[1:i])
            # Right subtree: all values > root_val
            right_subtree = bstFromPreorder(pre[i:])

            # Create the current node and attach subtrees
            return TreeNode(root_val, left_subtree, right_subtree)

        # Build the tree and return the root
        return bstFromPreorder(pre)


# Example usage:
# codec = Codec()
# root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
# serialized = codec.serialize(root)       # "5 3 2 4 7"
# deserialized = codec.deserialize(serialized)  # Rebuilds same BST
