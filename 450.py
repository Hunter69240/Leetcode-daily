class Solution:
    def deleteNode(self, root, key):
        """
        Deletes a node with given key from BST
        and returns updated root.
        """
        
        # -----------------------------------
        # Base Case
        # -----------------------------------
        if not root:
            return None
        
        # -----------------------------------
        # Step 1: Search for the node
        # -----------------------------------
        if key < root.val:
            # Key lies in left subtree
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            # Key lies in right subtree
            root.right = self.deleteNode(root.right, key)
        
        else:
            # -----------------------------------
            # Node Found → Perform Deletion
            # -----------------------------------
            
            # -----------------------------------
            # Case 1: No child (Leaf Node)
            # -----------------------------------
            if not root.left and not root.right:
                return None
            
            # -----------------------------------
            # Case 2: Only Right Child
            # -----------------------------------
            if not root.left:
                return root.right
            
            # -----------------------------------
            # Case 2: Only Left Child
            # -----------------------------------
            if not root.right:
                return root.left
            
            # -----------------------------------
            # Case 3: Two Children
            # -----------------------------------
            # Find Inorder Successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace current node value
            root.val = successor.val
            
            # Delete the successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)
        
        # Return updated root
        return root