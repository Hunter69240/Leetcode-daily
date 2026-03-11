# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Step 1: Initialize two pointers
        # slow moves 1 step at a time
        # fast moves 2 steps at a time
        slow = fast = head

        # Step 2: Detect if cycle exists
        # If there is a cycle, slow and fast will meet
        while fast and fast.next:
            slow = slow.next              # move slow by 1
            fast = fast.next.next         # move fast by 2

            # If both meet, cycle detected
            if slow == fast:
                break

        # If loop ended without meeting, no cycle
        else:
            return None

        # Step 3: Find the starting node of cycle
        # Move one pointer to head
        # Move both pointers 1 step at a time
        # The point where they meet again is cycle start
        while head != slow:
            head = head.next
            slow = slow.next

        # Step 4: Return the node where cycle begins
        return head
