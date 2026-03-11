# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # This method reorders a singly linked list in-place to follow the pattern:
        # first node, last node, second node, second last node, and so on.
        #
        # It uses the fast and slow pointer technique (also known as the "tortoise and hare" method)
        # to find the middle of the linked list efficiently.
        #
        # The process involves three main steps:
        # 1) Find the middle node using fast and slow pointers.
        # 2) Reverse the second half of the list starting right after the middle.
        # 3) Merge the two halves alternating nodes from each, to achieve the reordered list.

        # Initialize two pointers:
        # 'slow' moves one step at a time, 'fast' moves two steps at a time.
        # When 'fast' reaches the end, 'slow' will be at the middle of the list.
        slow, fast = head, head.next

        # Find the middle of the linked list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'second' is the start of the second half of the list (after middle).
        second = slow.next
        # Break the list into two halves by setting the end of the first half to None.
        prev = slow.next = None
        
        # Reverse the second half of the list.
        # Iteratively reverse the 'next' pointers to point backwards.
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 'first' points to the head of the first half, 'second' points to the head of reversed second half.
        first, second = head, prev

        # Merge the two halves by alternating nodes.
        while second:
            temp1, temp2 = first.next, second.next  # Store next nodes temporarily.
            first.next = second                      # Link current first node to current second node.
            second.next = temp1                      # Link current second node to the next node in the first half.
            first = temp1                           # Move to the next node in the first half.
            second = temp2                          # Move to the next node in the reversed second half.
