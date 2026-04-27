def a():
    s = "12"

    # dp[i] → number of ways to decode substring starting at index i
    # size = n + 1 to handle "jump beyond last index" cleanly
    dp = [0 for _ in range(len(s) + 1)]

    # dp[n] = 1
    # meaning: reaching end = 1 valid decoding (base case)
    dp[-1] = 1

    n = len(s)

    # iterate from right → left
    # because dp[i] depends on dp[i+1] and dp[i+2]
    for i in range(n - 1, -1, -1):
        print(i)

        # CASE 1: take single digit
        # valid only if current char is not '0'
        # because '0' cannot be decoded alone
        if s[i] != '0':
            dp[i] += dp[i + 1]
            # meaning:
            # take one step → number of ways = ways from next index

        # CASE 2: take two digits
        # must ensure:
        # - index exists
        # - number formed is between 10 and 26
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
            dp[i] += dp[i + 2]
            # meaning:
            # take two steps → add ways from i+2

    # dp[0] = total ways from start
    return dp[0]


# DRY RUN for "12"
#
# s = "12"
# n = 2
#
# dp initially = [0, 0, 1]
# index:          0  1  2
#
# i = 1 → s[1] = '2'
#
# - single digit valid → dp[1] += dp[2] = 1
# - no two-digit possible
#
# dp = [0, 1, 1]
#
#
# i = 0 → s[0] = '1'
#
# - single digit → dp[0] += dp[1] = 1
# - two digit "12" valid → dp[0] += dp[2] = 1
#
# dp = [2, 1, 1]
#
#
# FINAL:
# dp[0] = 2
#
# INTERPRETATION:
# "12" can be decoded as:
# "AB" (1,2)
# "L"  (12)
#
# CORE IDEA:
#
# At each index i:
# dp[i] = (ways from i+1 if valid) + (ways from i+2 if valid)
#
# This is counting number of paths from index i to end
#
print(a())

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         # DP dictionary where dp[i] = number of ways to decode from index i to end
#         # Base case: empty string (beyond the end) has 1 way to decode
#         dp = {len(s): 1}
        
#         # Iterate backwards from the end of the string to the beginning
#         for i in range(len(s) - 1, -1, -1):
#             # Case 1: If current digit is '0', it cannot be decoded alone
#             # (there's no letter mapping for '0')
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 # Current digit (1-9) can be decoded as a single digit
#                 # So inherit the number of ways from the next position
#                 dp[i] = dp[i + 1]

#             # Case 2: Check if we can form a valid two-digit number (10-26)
#             # Must have at least 2 characters remaining
#             if i + 1 < len(s) and (
#                 s[i] == "1" or  # 10-19 are all valid
#                 s[i] == "2" and s[i + 1] in "0123456"  # 20-26 are valid
#             ):
#                 # Add the ways from skipping 2 characters (decode as two-digit)
#                 dp[i] += dp[i + 2]
        
#         # Return the number of ways to decode from the start
#         return dp[0]
    