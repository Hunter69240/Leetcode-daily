class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def create_from_list(self, arr):
        if not arr:
            return

        self.head = Node(arr[0])
        current = self.head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

    
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def partition_list(self, x):
        # Dummy head for the list containing nodes with values < x
        before_node = Node(0)

        # Dummy head for the list containing nodes with values >= x
        after_node = Node(0)

        # Pointers to build the two lists
        before = before_node
        after = after_node

        # Pointer to traverse the original linked list
        curr = self.head

        # Traverse the original list
        while curr is not None:
            # If current node value is less than x,
            # append it to the 'before' list
            if curr.val < x:
                before.next = curr
                before = before.next
            # Otherwise, append it to the 'after' list
            else:
                after.next = curr
                after = after.next

            # Move to the next node in the original list
            curr = curr.next

        # Important step:
        # Terminate the 'after' list to avoid cycles
        after.next = None

        # Connect the 'before' list with the 'after' list
        before.next = after_node.next

        # Update head to the start of the partitioned list
        self.head = before_node.next




head = [1,4,3,2,5,2]
x=3
ll = LL()
ll.create_from_list(head)
ll.print_list()
ll.partition_list(x)
ll.print_list()