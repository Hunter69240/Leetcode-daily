def connect(self, root):

    # If tree is empty, nothing to connect
    if not root:
        return None

    # Start from root (first level)
    curr = root   

    # Outer loop → runs level by level
    while curr:

        # Dummy node helps build next level linked list
        dummy = Node(0)

        # Tail always points to last connected node
        tail = dummy

        # Inner loop → traverse current level using next pointers
        while curr:

            # If left child exists → attach to next level chain
            if curr.left:
                tail.next = curr.left   # Connect tail to left child
                tail = tail.next        # Move tail forward

            # If right child exists → attach to next level chain
            if curr.right:
                tail.next = curr.right  # Connect tail to right child
                tail = tail.next        # Move tail forward

            # Move horizontally in current level
            # (using already established next pointers)
            curr = curr.next

        # After finishing current level,
        # move down to the first node of next level
        curr = dummy.next

    # Return root after connections are made
    return root
