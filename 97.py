class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Basic check:
        # If the total length doesn't match, s3 cannot be an interleaving of s1 and s2
        if len(s1) + len(s2) != len(s3):
            return False
        
        # dp[i][j] means:
        #   Can s3[i + j:] be formed by interleaving s1[i:] and s2[j:] ?
        #
        # We build a (len(s1)+1) x (len(s2)+1) DP table initialized with False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        # Base case:
        # If we're at the end of both strings, it's a valid interleave
        dp[len(s1)][len(s2)] = True

        # Fill the table bottom-up, moving backwards from the ends of s1 and s2
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                # If next char of s1 matches the next required char in s3,
                # and the rest of the substring from dp[i+1][j] is valid,
                # then dp[i][j] is valid.
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True

                # Similarly, check if we can take the next char from s2
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        # dp[0][0] checks if FULL s3 can be formed from FULL s1 and s2
        return dp[0][0]
