def a():
    # Given two strings, goal:
    # Find length of longest sequence that appears in BOTH strings
    # while maintaining order (not necessarily continuous)

    text1 = "bsbininm"
    text2 = "jmjkbkjkv"

    # Optional swap:
    # Keeps first string longer (not required for correctness)
    if(len(text1) < len(text2)):
        text1, text2 = text2, text1

    # DP dimensions:
    # +1 is used to represent empty prefix ("")
    rows = len(text1) + 1
    cols = len(text2) + 1

    # dp[i][j] means:
    # LCS length using first i characters of text1
    # and first j characters of text2
    #
    # Example:
    # dp[3][2] → LCS of text1[:3] and text2[:2]
    dp = [[0] * cols for _ in range(rows)]

    # Iterate over characters (0-based access)
    # NOTE: This implementation uses i, j directly on strings,
    # so dp indexing is slightly shifted logically
    for i in range(rows - 1):
        for j in range(cols - 1):

            # If characters match:
            # We can include this character in subsequence
            # So extend previous best (diagonal)
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                # If characters don't match:
                # We must drop one character
                #
                # dp[i-1][j] → drop from text1
                # dp[i][j-1] → drop from text2
                #
                # Take the better option
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Returns last computed cell (due to loop variables)
    # Intended meaning: final LCS length
    return dp[i][j]


# DRY RUN SUMMARY:
#
# text1 = "bsbininm"
# text2 = "jmjkbkjkv"
#
# Most characters do not match → dp values stay 0
#
# Only match occurs at:
# 'm' in text1 and 'm' in text2
#
# At that point:
# dp[i][j] = 1 + previous diagonal = 1
#
# After that, values propagate using max()
#
# Final result = 1
#
# INTERPRETATION:
# Longest common subsequence is of length 1 ("m")
#
# CORE IDEA:
#
# dp[i][j] stores:
# "Best subsequence length possible using prefixes up to i and j"
#
# Transition:
# - match → extend subsequence (diagonal +1)
# - mismatch → choose best previous (max of left/up)
#
# WHY DP:
# Same prefix combinations repeat → store results to avoid recomputation
#
print(a())



# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # Create a 2D DP table with dimensions (len(text1)+1) x (len(text2)+1)
#         # Extra row and column are initialized to 0 to handle base cases
#         dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)] 

#         # Iterate backwards through text1 (from last character to first)
#         for i in range(len(text1)-1, -1, -1):
#             # Iterate backwards through text2 (from last character to first)
#             for j in range(len(text2)-1, -1, -1):
#                 # If characters at current positions match
#                 if text1[i] == text2[j]:
#                     # Include this character in LCS
#                     # Add 1 to the result from the next diagonal cell (i+1, j+1)
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                 else:
#                     # Characters don't match, so take the maximum of:
#                     # - Skipping current character in text2 (move right: dp[i][j+1])
#                     # - Skipping current character in text1 (move down: dp[i+1][j])
#                     dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
#         # Return the LCS length stored at dp[0][0]
#         # This represents the LCS of the full text1 and text2
#         return dp[0][0]
