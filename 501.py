class Solution:
    def findMode(self, root):
        """
        Approach 1:
        Count frequency using dictionary.
        Works for ANY binary tree (not just BST).
        """

        freq_map = {}
        maxFreq = 0
        result = []

        def dfs(node):
            nonlocal maxFreq

            if not node:
                return

            # Update frequency
            freq_map[node.val] = freq_map.get(node.val, 0) + 1

            # Update max frequency
            maxFreq = max(maxFreq, freq_map[node.val])

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Collect all values with max frequency
        for value, freq in freq_map.items():
            if freq == maxFreq:
                result.append(value)

        return result