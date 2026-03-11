def longestSubstring(s, k):
    # ---------------------------------------------------------
    # PROBLEM:
    # Given a string s and an integer k, return the length of
    # the longest substring such that every character in the
    # substring appears at least k times.
    #
    # Example:
    # s = "aaabb", k = 3
    # Output = 3  → substring "aaa"
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # BASE CASE:
    # If string length is smaller than k, it is impossible
    # for any character to appear k times.
    # ---------------------------------------------------------
    if len(s) < k:
        return 0

    # ---------------------------------------------------------
    # STEP 1: COUNT FREQUENCY OF EACH CHARACTER
    # ---------------------------------------------------------
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # ---------------------------------------------------------
    # STEP 2: CHECK FOR INVALID CHARACTERS
    #
    # If any character appears fewer than k times,
    # that character CANNOT be part of a valid substring.
    # ---------------------------------------------------------
    for ch in freq:
        if freq[ch] < k:

            # -------------------------------------------------
            # STEP 3: SPLIT STRING USING INVALID CHARACTER
            #
            # Since `ch` is invalid, any valid substring must
            # lie completely in one of the split parts.
            # -------------------------------------------------
            max_len = 0
            for part in s.split(ch):
                # Recursively solve for each part
                max_len = max(max_len, longestSubstring(part, k))

            # -------------------------------------------------
            # Return the maximum valid substring length found
            # -------------------------------------------------
            return max_len

    # ---------------------------------------------------------
    # STEP 4: ALL CHARACTERS ARE VALID
    #
    # If we never found a character with freq < k,
    # the entire string is valid.
    # ---------------------------------------------------------
    return len(s)


# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------
s = "aaabb"
k = 3

# ---------------------------------------------------------
# FUNCTION CALL
# ---------------------------------------------------------
print(longestSubstring(s, k))  # Output: 3

# ---------------------------------------------------------
# DRY RUN:
#
# s = "aaabb", k = 3
#
# Frequencies:
# a → 3
# b → 2  (invalid, since 2 < 3)
#
# Split on 'b':
# s.split('b') → ["aaa", "", ""]
#
# Recursive calls:
# longestSubstring("aaa", 3) → valid → length = 3
# longestSubstring("", 3)    → length < k → 0
#
# max(3, 0, 0) = 3
#
# Final Answer = 3
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# Worst case → O(n²) due to repeated splitting and recursion
#
# AVERAGE CASE:
# Much faster due to pruning invalid characters early
#
# SPACE COMPLEXITY:
# O(n) due to recursion stack and substrings
# ---------------------------------------------------------
