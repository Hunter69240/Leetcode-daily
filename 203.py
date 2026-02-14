head_values = [1, 2, 6, 3, 4, 5, 6]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LL:
    def __init__(self):
        self.head = None

    # Build linked list from a Python list
    def build_from_list(self, values):
        if not values:
            return
        
        self.head = ListNode(values[0])
        current = self.head

        for value in values[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = new_node

    # Print linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def remove_value(self, value):

        # Create a dummy node before head
        # This helps handle edge case when head itself needs to be removed
        dummy = ListNode(0)

        # Point dummy to current head
        dummy.next = self.head

        # curr → used to traverse the list
        curr = self.head

        # prev → keeps track of previous node
        # Initially points to dummy
        prev = dummy

        # Traverse the linked list
        while curr:

            # If current node value matches the target value
            if curr.val == value:

                # Skip the current node
                # (remove it by changing prev.next)
                prev.next = curr.next

                # Move curr forward
                # (prev stays same because we removed curr)
                curr = curr.next

            else:
                # Move prev forward only when we DO NOT delete
                prev = curr

                # Move curr forward
                curr = curr.next

        # Return new head (could change if original head was removed)
        return dummy.next



# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":
    ll = LL()

    print("Building Linked List...")
    ll.build_from_list(head_values)

    print("Printing Linked List:")
    ll.print_list()
