class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D DP table with dimensions (len(text1)+1) x (len(text2)+1)
        # Extra row and column are initialized to 0 to handle base cases
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)] 

        # Iterate backwards through text1 (from last character to first)
        for i in range(len(text1)-1, -1, -1):
            # Iterate backwards through text2 (from last character to first)
            for j in range(len(text2)-1, -1, -1):
                # If characters at current positions match
                if text1[i] == text2[j]:
                    # Include this character in LCS
                    # Add 1 to the result from the next diagonal cell (i+1, j+1)
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # Characters don't match, so take the maximum of:
                    # - Skipping current character in text2 (move right: dp[i][j+1])
                    # - Skipping current character in text1 (move down: dp[i+1][j])
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        # Return the LCS length stored at dp[0][0]
        # This represents the LCS of the full text1 and text2
        return dp[0][0]
