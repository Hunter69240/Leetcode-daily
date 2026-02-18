class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        :type root: TreeNode
        :rtype: None
        Do not return anything, modify tree in-place instead.
        """

        # These will help us detect the two swapped nodes
        self.first = None     # First incorrect node
        self.second = None    # Second incorrect node
        self.prev = None      # Previous node in inorder traversal
        
        def inorder(node):
            # Base case
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # -----------------------------
            # Detect BST violation
            # In a correct BST:
            # inorder traversal should be strictly increasing
            # prev.val should always be < current node.val
            # -----------------------------
            
            if self.prev and self.prev.val > node.val:
                
                # First time violation detected
                if not self.first:
                    # Store the previous node
                    # This is the first misplaced node
                    self.first = self.prev
                
                # Always update second
                # This handles both adjacent & non-adjacent swaps
                self.second = node
            
            # Move prev forward
            self.prev = node
            
            # Traverse right subtree
            inorder(node.right)
        
        # Perform inorder traversal
        inorder(root)
        
        # Swap values of the two incorrect nodes
        self.first.val, self.second.val = self.second.val, self.first.val
