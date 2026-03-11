class Solution:
    def numDecodings(self, s: str) -> int:
        # DP dictionary where dp[i] = number of ways to decode from index i to end
        # Base case: empty string (beyond the end) has 1 way to decode
        dp = {len(s): 1}
        
        # Iterate backwards from the end of the string to the beginning
        for i in range(len(s) - 1, -1, -1):
            # Case 1: If current digit is '0', it cannot be decoded alone
            # (there's no letter mapping for '0')
            if s[i] == "0":
                dp[i] = 0
            else:
                # Current digit (1-9) can be decoded as a single digit
                # So inherit the number of ways from the next position
                dp[i] = dp[i + 1]

            # Case 2: Check if we can form a valid two-digit number (10-26)
            # Must have at least 2 characters remaining
            if i + 1 < len(s) and (
                s[i] == "1" or  # 10-19 are all valid
                s[i] == "2" and s[i + 1] in "0123456"  # 20-26 are valid
            ):
                # Add the ways from skipping 2 characters (decode as two-digit)
                dp[i] += dp[i + 2]
        
        # Return the number of ways to decode from the start
        return dp[0]
    