class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # INTUITION: Bottom-up DP approach - work backwards from end of string
        # dp[i] = True if substring from index i to end can be segmented into valid words
        # If we can match a word at position i AND the rest after it is valid, then i is valid
        
        # Initialize DP array with False for all positions
        dp = [False] * (len(s) + 1)
        
        # Base case: empty string (position beyond last char) is always valid
        # This represents successfully reaching the end of the string
        dp[len(s)] = True

        # Iterate backwards through the string from last character to first
        # Building up solutions for larger substrings using smaller ones
        for i in range(len(s) - 1, -1, -1):
            
            # Try matching each word in dictionary at current position i
            for w in wordDict:
                
                # Check two conditions:
                # 1. Word doesn't exceed string boundary: (i + len(w)) <= len(s)
                # 2. Substring at position i matches the word: s[i:i+len(w)] == w
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    
                    # If word matches, check if remainder of string is valid
                    # dp[i] inherits the validity of position after the word ends
                    dp[i] = dp[i + len(w)]
                
                # Early exit optimization: if we found a valid segmentation,
                # no need to check other words at this position
                if dp[i]:
                    break
        
        # Return whether entire string (starting from index 0) can be segmented
        return dp[0]
