class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []   # Final result: list of all palindrome partitions
        part = []  # Current partition being built (list of substrings)

        # Depth-first search function starting from index i
        def dfs(i):
            # If we've reached the end of the string, add current partition
            if i >= len(s):
                res.append(part.copy())  # Use copy() to avoid reference issues
                return

            # Try all possible substrings starting at index i
            for j in range(i, len(s)):
                # Check if substring s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    # Choose: add the palindrome substring to current path
                    part.append(s[i:j+1])
                    
                    # Explore: recurse for the remaining substring
                    dfs(j+1)
                    
                    # Un-choose (backtrack): remove the last added substring
                    part.pop()

        # Start DFS from index 0
        dfs(0)
        return res

    # Helper function to check if s[l:r] is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:   # If mismatch, not a palindrome
                return False
            l, r = l + 1, r - 1  # Move inward
        return True  # No mismatches → palindrome
