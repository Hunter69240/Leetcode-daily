# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # This method reverses nodes of a linked list k at a time.
        # If the number of nodes is not a multiple of k, 
        # the last remaining nodes are left as is.
        #
        # The reversal is done in-place by changing node pointers.
        # Steps:
        # 1) Use a dummy node to simplify edge cases.
        # 2) For each group of k nodes, reverse all k nodes.
        # 3) Link the reversed group back to the previous part.
        # 4) Move forward to the next group until less than k nodes remain.

        dummy = ListNode(0, head)
        # Dummy node points to head; helps maintain references on head changes.
        groupPrev = dummy
        # 'groupPrev' tracks the node before the current k-group to reverse.

        while True:
            # Find the kth node from groupPrev to mark the group's end.
            kth = self.getKth(groupPrev, k)
            if not kth:
                # Less than k nodes remain; so done reversing.
                break

            groupNext = kth.next
            # 'groupNext' is the node right after the kth node (start of next group).

            # Reverse nodes in the group iteratively.
            prev, curr = kth.next, groupPrev.next  
            # Start reversing from first node in group; 'prev' initially points to groupNext.

            while curr != groupNext:
                temp = curr.next        # Store next node temporarily.
                curr.next = prev        # Reverse current node's pointer to previous node.
                prev = curr             # Move prev forward to current node.
                curr = temp             # Move curr forward to next node.

            # After reversal:
            # 'groupPrev.next' is the start of the original group (now the last node in reversed group).
            # 'kth' is the new head of reversed group.

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            # Reconnect previous part of list to reversed group's head (kth).
            # 'groupPrev' moves to the tail of the reversed group to link next part in the next iteration.

        return dummy.next
        # Return the new head of the reversed list (after dummy).

    def getKth(self, curr, k):
        # Helper method to find the kth node starting from 'curr'.
        # Moves k steps forward and returns the node.
        # Returns None if fewer than k nodes remain.

        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
