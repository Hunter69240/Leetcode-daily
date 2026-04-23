def a():
    # Problem:
    # Check if the string can be segmented into valid dictionary words.

    s = "leetcode"
    wordDict = ["leet", "code"]

    # DP Definition:
    # dp[i] = True → s[0:i] can be formed using words
    dp = [False for _ in range(len(s) + 1)]

    # Base case:
    # Empty string is valid
    dp[0] = True

    # Iterate over prefix lengths
    for i in range(len(s) + 1):

        # Try all possible last cuts
        for j in range(i):

            # Check:
            # 1. prefix till j is valid
            # 2. substring from j to i is a word
            if dp[j] == True and s[j:i] in wordDict:
                dp[i] = True
                break

        # ---- DRY RUN ----
        # s = "leetcode"
        #
        # i = 0 → "" → already True (base case)
        #
        # i = 1 → "l"
        #   j = 0 → dp[0]=True, "l" not in dict → dp[1]=False
        #
        # i = 2 → "le"
        #   j = 0 → "le" not in dict
        #   j = 1 → dp[1]=False
        #   → dp[2]=False
        #
        # i = 3 → "lee"
        #   all splits invalid → dp[3]=False
        #
        # i = 4 → "leet"
        #   j = 0 → dp[0]=True, "leet" in dict → dp[4]=True
        #
        # i = 5 → "leetc"
        #   j = 0 → "leetc" not word
        #   j = 4 → dp[4]=True, "c" not word
        #   → dp[5]=False
        #
        # i = 6 → "leetco"
        #   j = 4 → dp[4]=True, "co" not word
        #   → dp[6]=False
        #
        # i = 7 → "leetcod"
        #   j = 4 → "cod" not word
        #   → dp[7]=False
        #
        # i = 8 → "leetcode"
        #   j = 4 → dp[4]=True, "code" in dict → dp[8]=True
        #
        # Final dp:
        # [True, False, False, False, True, False, False, False, True]

    # Final result: can full string be formed
    print(dp[len(s)])


print(a())


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # INTUITION: Bottom-up DP approach - work backwards from end of string
#         # dp[i] = True if substring from index i to end can be segmented into valid words
#         # If we can match a word at position i AND the rest after it is valid, then i is valid
        
#         # Initialize DP array with False for all positions
#         dp = [False] * (len(s) + 1)
        
#         # Base case: empty string (position beyond last char) is always valid
#         # This represents successfully reaching the end of the string
#         dp[len(s)] = True

#         # Iterate backwards through the string from last character to first
#         # Building up solutions for larger substrings using smaller ones
#         for i in range(len(s) - 1, -1, -1):
            
#             # Try matching each word in dictionary at current position i
#             for w in wordDict:
                
#                 # Check two conditions:
#                 # 1. Word doesn't exceed string boundary: (i + len(w)) <= len(s)
#                 # 2. Substring at position i matches the word: s[i:i+len(w)] == w
#                 if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    
#                     # If word matches, check if remainder of string is valid
#                     # dp[i] inherits the validity of position after the word ends
#                     dp[i] = dp[i + len(w)]
                
#                 # Early exit optimization: if we found a valid segmentation,
#                 # no need to check other words at this position
#                 if dp[i]:
#                     break
        
#         # Return whether entire string (starting from index 0) can be segmented
#         return dp[0]
