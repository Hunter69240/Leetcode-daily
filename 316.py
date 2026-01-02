s = "cbacdcbc"

i = 1
res = [s[0]]

while i < len(s):
    if s[i] in res:
        i += 1
        continue

    while res and s[i] < res[-1] and res[-1] in s[i:]:
        res.pop()

    res.append(s[i])
    i += 1

print("".join(res))


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "Remove Duplicate Letters" problem.
#
# Goal:
# - Remove duplicate letters so that every letter appears ONCE
# - The resulting string must be the SMALLEST in lexicographical order
#
# Key ideas:
# - Use a stack-like list `res`
# - Maintain increasing lexicographical order when possible
# - Only remove a character if it appears again later
#
# Why stack?
# - We want to undo (pop) previous choices if a better
#   lexicographical choice appears later.
# ---------------------------------------------------------

# ---------------------------------------------------------
# CONDITIONS EXPLAINED:
#
# if s[i] in res:
#   → skip duplicates (each character allowed only once)
#
# while res and s[i] < res[-1] and res[-1] in s[i:]:
#   → res[-1] is bigger than current char
#   → AND it appears again later
#   → so it is safe to remove it now
#
# This ensures:
# - lexicographically smallest result
# - no character is lost permanently
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "cbacdcbc"
#
# Start:
# res = ['c']
#
# i=1 → 'b'
# 'b' < 'c' AND 'c' appears later → pop 'c'
# res = []
# append 'b'
# res = ['b']
#
# i=2 → 'a'
# 'a' < 'b' AND 'b' appears later → pop 'b'
# res = []
# append 'a'
# res = ['a']
#
# i=3 → 'c'
# 'c' > 'a' → append
# res = ['a','c']
#
# i=4 → 'd'
# 'd' > 'c' → append
# res = ['a','c','d']
#
# i=5 → 'c'
# already in res → skip
#
# i=6 → 'b'
# 'b' < 'd' BUT 'd' does NOT appear later → cannot pop
# 'b' < 'c' AND 'c' appears later → pop 'c'
# res = ['a','d']
# append 'b'
# res = ['a','d','b']
#
# i=7 → 'c'
# append
# res = ['a','d','b','c']
#
# FINAL RESULT:
# "adbc"
#
# (Lexicographically smallest string with unique letters)
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME & SPACE COMPLEXITY:
#
# Time:  O(n²) due to `res[-1] in s[i:]`
# Space: O(n)
#
# NOTE:
# This can be optimized to O(n) using a frequency map.
# ---------------------------------------------------------
