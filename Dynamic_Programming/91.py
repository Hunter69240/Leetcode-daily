def a():
    s = "12"

    # Think of it like this:
    # you are standing at each digit and asking
    # "how many ways can I decode from HERE to the END?"
    # dp[i] stores that answer for each position i
    dp = [0 for _ in range(len(s) + 1)]

    # BASE CASE: you've reached the end (nothing left to decode)
    # that itself counts as 1 successful decoding
    # like in climbing stairs → you successfully reached the top
    dp[-1] = 1

    n = len(s)

    # we go RIGHT TO LEFT because
    # to answer "how many ways from position i"
    # we need to already know "how many ways from i+1 and i+2"
    # so we solve the end first, then work backwards
    for i in range(n - 1, -1, -1):

        # CHOICE 1: take current digit ALONE
        # example: at '1' in "12" → take just '1' (= A)
        # remaining string starts at i+1
        # so add however many ways exist from i+1
        #
        # BUT: '0' can never be taken alone (no letter maps to 0)
        # so skip this choice if current digit is '0'
        if s[i] != '0':
            dp[i] += dp[i + 1]
            #            ↑
            #    you consumed 1 digit
            #    so remaining string starts 1 position ahead

        # CHOICE 2: take current digit + next digit TOGETHER
        # example: at '1' in "12" → take '1' and '2' together as 12 (= L)
        # remaining string starts at i+2
        # so add however many ways exist from i+2
        #
        # BUT two conditions must be true:
        # condition 1 → i+1 must exist (cant go out of bounds)
        # condition 2 → the two digits must form a number between 10-26
        #               starts with '1' → always valid (10-19)
        #               starts with '2' → only valid if next digit <= '6' (20-26)
        #               starts with anything else → invalid (would exceed 26)
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
            dp[i] += dp[i + 2]
            #            ↑
            #    you consumed 2 digits
            #    so remaining string starts 2 positions ahead

    return dp[0]
    # dp[0] = total ways to decode the entire string
    # because it answers "how many ways from position 0 to end?"


# ─────────────────────────────────────────
# DRY RUN for s = "12"
# ─────────────────────────────────────────
#
# initial dp = [0, 0, 1]
# index:        0  1  2
#                        ↑ base case: empty string = 1 way
#
# ── i = 1, digit = '2' ──
#
#   CHOICE 1: take '2' alone
#   '2' != '0' ✅
#   dp[1] += dp[2] → dp[1] = 0 + 1 = 1
#
#   CHOICE 2: take two digits
#   i+1 = 2, which is NOT < n (2 < 2 is false) ❌
#   no next digit exists, skip
#
# dp = [0, 1, 1]
#
# ── i = 0, digit = '1' ──
#
#   CHOICE 1: take '1' alone
#   '1' != '0' ✅
#   dp[0] += dp[1] → dp[0] = 0 + 1 = 1
#   meaning: take '1' alone, then decode "2" → 1 way
#
#   CHOICE 2: take '1' and '2' together as 12
#   i+1 = 1 < 2 ✅ and s[0] == '1' ✅
#   dp[0] += dp[2] → dp[0] = 1 + 1 = 2
#   meaning: take '12' together, then decode "" → 1 way
#
# dp = [2, 1, 1]
#
# ─────────────────────────────────────────
# FINAL ANSWER: dp[0] = 2
#
# the 2 decodings are:
#   "1","2"  → A, B  → "AB"
#   "12"     → L     → "L"
#
# ─────────────────────────────────────────
# THE ONE QUESTION THAT SOLVES ALL LINEAR DP:
#
#   "At this position, what are my choices
#    and where does each choice take me?"
#
#   take 1 digit → go to i+1 → add dp[i+1]
#   take 2 digits → go to i+2 → add dp[i+2]
#
# same exact thinking as climbing stairs:
#   take 1 step → go to i+1 → add dp[i+1]
#   take 2 steps → go to i+2 → add dp[i+2]
# ─────────────────────────────────────────
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
    