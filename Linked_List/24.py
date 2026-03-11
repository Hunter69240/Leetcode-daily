# Node of a Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list from array
    def create_from_list(self, arr):
        if not arr:
            return

        self.head = Node(arr[0])
        current = self.head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

    # Print linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def swap_nodes(self):
        # Dummy node to handle edge cases (like swapping from head)
        dummy = Node(0)
        dummy.next = self.head

        # prev points to the node before the current pair
        prev = dummy

        # Traverse while there are at least two nodes to swap
        while prev.next and prev.next.next:
            # First node of the pair
            first = prev.next

            # Second node of the pair
            second = first.next

            # Perform the swap
            first.next = second.next   # first points to node after the pair
            second.next = first        # second points to first
            prev.next = second         # prev points to second (new head of pair)

            # Move prev to the end of the swapped pair
            prev = first

        # Update head to new starting node
        self.head = dummy.next



head = [1, 2, 3, 4]

ll = LinkedList()
ll.create_from_list(head)
ll.print_list()
ll.swap_nodes()
ll.print_list()

