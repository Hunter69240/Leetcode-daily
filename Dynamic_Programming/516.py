# Longest Palindromic Subsequence - LC 516
# Key insight: Subsequence = can skip characters = CHOICES = DP
# Look at corners i and j each time:
#   If match   → both contribute, move both inward
#   If no match → skip one end, take the best of both choices
# Base cases:
#   i > j → empty string → 0
#   i == j → single character → always palindrome of length 1


"""
This is Interval DP because the problem asks for subsequence (can skip), and when corners don't match I have two choices — shrink from left or shrink from right — and take the best of both.
"""


def longestPalSubseq(s):
    memo = {}

    def solve(s, i, j):
        if (i, j) in memo:  # already computed this subproblem
            return memo[(i, j)]
        if i > j:  # empty string, no characters left
            memo[(i, j)] = 0
            return 0
        if i == j:  # single character, always palindrome
            memo[(i, j)] = 1
            return 1
        if s[i] == s[j]:  # both corners match!
            a = 2 + solve(s, i + 1, j - 1)  # count both + solve middle
            memo[(i, j)] = a
            return a
        if s[i] != s[j]:  # corners don't match, have 2 choices
            a = max(
                solve(s, i, j - 1),  # choice 1: skip right character
                solve(s, i + 1, j),
            )  # choice 2: skip left character
            memo[(i, j)] = a
            return a

    return solve(s, 0, len(s) - 1)  # start with full string
