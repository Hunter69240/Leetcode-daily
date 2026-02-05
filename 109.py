class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Base case: empty linked list
        if not head:
            return None

        # Base case: single node becomes a leaf in BST
        if not head.next:
            return TreeNode(head.val)

        # Slow & fast pointers to find middle of the list
        slow, fast = head, head

        # Pointer to keep track of node before 'slow'
        slow_prev = None

        # 1️⃣ Find the middle node of the linked list
        # slow moves 1 step, fast moves 2 steps
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Middle node becomes root of BST
        root = TreeNode(slow.val)

        # 3️⃣ Disconnect left half from the middle node
        # This splits the list into two halves
        slow_prev.next = None

        # 4️⃣ Recursively build left subtree from left half
        root.left = self.sortedListToBST(head)

        # 5️⃣ Recursively build right subtree from right half
        root.right = self.sortedListToBST(slow.next)

        # Return constructed BST root
        return root
