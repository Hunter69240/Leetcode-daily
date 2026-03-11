"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Each Node has a value and a list of neighbors (adjacent nodes).
# If neighbors are not provided, initialize with an empty list.


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        oldToNew = {}  
        # Dictionary to map original nodes -> their cloned copies.
        # Helps in avoiding duplicate copies and handling cycles.

        def dfs(node):
            # If this node is already cloned, return its clone
            if node in oldToNew:
                return oldToNew[node]   
            
            # Create a copy of the current node
            copy = Node(node.val)
            
            # Store it in the map before exploring neighbors 
            # (important to avoid infinite recursion in cycles)
            oldToNew[node] = copy

            # Recursively clone and connect all neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        # If input is None, return None
        return dfs(node) if node else None
