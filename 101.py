from collections import deque

def isSymmetric(self, root):
    # If tree is empty, it is symmetric
    if not root:
        return True

    # Create a queue to store pairs of nodes to compare
    queue = deque()

    # Start by comparing left and right subtree of root
    queue.append((root.left, root.right))

    # Process until queue becomes empty
    while queue:

        # Pop the front pair of nodes
        node1, node2 = queue.popleft()

        # Case 1: Both nodes are None → symmetric at this level
        if not node1 and not node2:
            continue   # move to next pair

        # Case 2: One is None and other is not → not symmetric
        if not node1 or not node2:
            return False

        # Case 3: Values are different → not symmetric
        if node1.val != node2.val:
            return False

        # Add children in mirror order
        # Left of node1 must match Right of node2
        queue.append((node1.left, node2.right))

        # Right of node1 must match Left of node2
        queue.append((node1.right, node2.left))

    # If all comparisons passed → symmetric
    return True