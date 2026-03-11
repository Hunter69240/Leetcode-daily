# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # ---------------------------------------------------------
        # EXPLANATION:
        # We sort a linked list using MERGE SORT.
        #
        # Why merge sort?
        # - Linked lists do not support random access.
        # - Merge sort works well with sequential access.
        # - Time complexity: O(n log n)
        # - Space complexity: O(log n) due to recursion
        #
        # Steps:
        # 1) Split the linked list into two halves using slow/fast pointers
        # 2) Recursively sort both halves
        # 3) Merge the two sorted halves
        # ---------------------------------------------------------

        # Base case:
        # If the list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head

        # ---------------------------------------------------------
        # STEP 1: SPLIT THE LIST INTO TWO HALVES
        #
        # Use slow and fast pointers:
        # - slow moves 1 step
        # - fast moves 2 steps
        #
        # When fast reaches the end,
        # slow will be at the midpoint.
        # ---------------------------------------------------------

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid is the start of the second half
        mid = slow.next

        # break the list into two halves
        slow.next = None

        # ---------------------------------------------------------
        # DRY RUN (SPLITTING):
        #
        # head: 4 -> 2 -> 1 -> 3
        #
        # slow stops at 2
        #
        # left half:  4 -> 2
        # right half: 1 -> 3
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # STEP 2: RECURSIVELY SORT BOTH HALVES
        # ---------------------------------------------------------

        left = self.sortList(head)
        right = self.sortList(mid)

        # ---------------------------------------------------------
        # STEP 3: MERGE THE TWO SORTED HALVES
        # ---------------------------------------------------------

        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:

        # ---------------------------------------------------------
        # EXPLANATION:
        # This function merges two sorted linked lists
        # into one sorted linked list.
        #
        # Uses a dummy node to simplify pointer handling.
        # ---------------------------------------------------------

        dummy = ListNode(0)
        tail = dummy

        # ---------------------------------------------------------
        # DRY RUN (MERGING):
        #
        # l1: 2 -> 4
        # l2: 1 -> 3
        #
        # Compare 2 and 1 → take 1
        # Compare 2 and 3 → take 2
        # Compare 4 and 3 → take 3
        # Attach remaining → 4
        #
        # Result: 1 -> 2 -> 3 -> 4
        # ---------------------------------------------------------

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes (only one of them is non-null)
        tail.next = l1 if l1 else l2

        return dummy.next
