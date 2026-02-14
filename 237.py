class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        Do not return anything, modify node in-place instead.
        """

        # We are NOT given the head of the list.
        # We are only given the node that needs to be deleted.
        # Important: This node is guaranteed NOT to be the last node.

        curr = node   # Current node is the node to delete

        # Step 1:
        # Copy the value of next node into current node
        curr.val = curr.next.val

        # Step 2:
        # Skip the next node (remove it from list)
        curr.next = curr.next.next
