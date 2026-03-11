from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string using Level Order Traversal (BFS)
        """
        if not root:
            return "null"

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                # Store current node value
                res.append(str(node.val))

                # Push children (even if they are None)
                q.append(node.left)
                q.append(node.right)
            else:
                # Store null to preserve structure
                res.append("null")

        return ",".join(res)


    def deserialize(self, data):
        """
        Decodes string back to tree using BFS
        """
        if data == "null":
            return None

        nodes = data.split(",")

        # Create root node
        root = TreeNode(int(nodes[0]))
        q = deque([root])

        i = 1  # Pointer for nodes list

        while q:
            curr = q.popleft()

            # Process LEFT child
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1

            # Process RIGHT child
            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1

        return root