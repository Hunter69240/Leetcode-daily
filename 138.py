# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)         # Node's value
        self.next = next          # Pointer to the next node in the list
        self.random = random      # Pointer to a random node in the list (could be None)


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        # Create a dictionary to map each original node to its copied node.
        # Also map None to None to simplify assigning next/random pointers later.

        cur = head
        # Start traversing the original linked list from the head.

        # First pass: create new copy nodes (with the same value) for each original node.
        # Store the mapping from original node to its copy in the dictionary.
        while cur:
            copy = Node(cur.val)    # Create a copy with the current node's value
            oldToCopy[cur] = copy   # Map the original node to this new copy
            cur = cur.next          # Move to the next node in the original list

        cur = head  
        # Start from the head again to set next and random pointers for the copied nodes.

        # Second pass: assign the next and random pointers for each copied node.
        while cur:
            copy = oldToCopy[cur]                      # Retrieve copied node corresponding to original node
            copy.next = oldToCopy[cur.next]            # Set copied node's next pointer
            copy.random = oldToCopy[cur.random]        # Set copied node's random pointer
            cur = cur.next                            # Move to the next node in the original list

        # Return the copied head node, which starts the deep copied linked list.
        return oldToCopy[head]
