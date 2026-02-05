class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class ListNode:
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

    
    def reverse_list(self, left, right):
        # If list is empty or no reversal needed
        if not self.head or left == right:
            return self.head

        # Dummy node to handle edge cases
        # (especially when left == 1)
        dummy = Node(0)
        dummy.next = self.head

        # Pointer to reach node just before 'left'
        before = dummy

        # Pointer that will point to the 'left' node
        curr = self.head

        # 1️⃣ Move 'before' and 'curr' to correct positions
        # 'before' → node just before 'left'
        # 'curr'   → node at position 'left'
        for _ in range(left - 1):
            before = curr
            curr = curr.next

        # 2️⃣ Find the node just after position 'right'
        temp = curr
        for _ in range(right - left):
            temp = temp.next
        after = temp.next

        # 3️⃣ Reverse the sublist from 'left' to 'right'
        # 'prev' starts from 'after' to reconnect later
        prev = after
        while curr is not after:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 4️⃣ Reconnect the reversed sublist with the main list
        before.next = prev

        # Update head in case left == 1
        self.head = dummy.next

head = [3,5]
left = 1
right = 2
ll=ListNode()
ll.create_from_list(head)
ll.print_list()
ll.reverse_list(left,right)
ll.print_list()
