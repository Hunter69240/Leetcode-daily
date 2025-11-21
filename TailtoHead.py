# Node class definition
class Node:
    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # Pointer to the next node

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, set new_node as head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end and append
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node  # Link the last node to the new node

    def print_list(self):
        # Print all elements of the linked list
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def move_tail_to_head(self):
        curr = self.head

        # If list is empty or has only one node, nothing to do
        if curr is None or curr.next is None:
            return

        # Traverse to the last node while tracking the previous node
        while curr.next:
            prev = curr
            curr = curr.next

        # At this point, curr is the tail and prev is the second-last node
        prev.next = None       # Detach the last node (tail)
        curr.next = self.head  # Point tail node to the old head
        self.head = curr       # Update head to be the former tail

# Create linked list and add nodes A, B, C, D
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# Print the original linked list
llist.print_list()

print("after moving tail to head:")

# Move the tail node to the front of the list
llist.move_tail_to_head()

# Print the modified linked list
llist.print_list()
