class Solution:
    def pathSum(self, root, targetSum):
        """
        Returns number of paths where sum of nodes equals targetSum.
        Path must go downward (parent → child).
        """
        
        # -----------------------------------
        # Step 0: Prefix HashMap Initialization
        # -----------------------------------
        # {prefix_sum : frequency}
        # Base case → sum 0 seen once
        # This handles path starting from root
        prefix = {0: 1}
        
        # Stores total valid paths
        self.count = 0
        
        # -----------------------------------
        # DFS Function
        # -----------------------------------
        def dfs(node, currentSum):
            if not node:
                return
            
            # -----------------------------------
            # Step 1: Update Running Sum
            # -----------------------------------
            currentSum += node.val
            
            # -----------------------------------
            # Step 2: Check if valid path exists
            # We need:
            # currentSum - oldPrefix = targetSum
            # → oldPrefix = currentSum - targetSum
            # -----------------------------------
            needed = currentSum - targetSum
            
            if needed in prefix:
                self.count += prefix[needed]
            
            # -----------------------------------
            # Step 3: Store Current Prefix Sum
            # -----------------------------------
            prefix[currentSum] = prefix.get(currentSum, 0) + 1
            
            # -----------------------------------
            # Step 4: Explore Left & Right
            # -----------------------------------
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
            
            # -----------------------------------
            # Step 5: Backtrack
            # Remove current sum before returning
            # -----------------------------------
            prefix[currentSum] -= 1
        
        # Start DFS from root with sum 0
        dfs(root, 0)
        
        return self.count