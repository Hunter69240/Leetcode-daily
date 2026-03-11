s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# ---------------------------------------------------------
# PROBLEM:
# Given a DNA string s, find all 10-letter-long sequences
# (substrings) that occur more than once.
#
# DNA characters consist of:
# 'A', 'C', 'G', 'T'
# ---------------------------------------------------------

# ---------------------------------------------------------
# dict → stores frequency of each 10-length substring
# res  → stores repeated substrings
# ---------------------------------------------------------
dict = {}
res = []

# ---------------------------------------------------------
# STEP 1: GENERATE ALL SUBSTRINGS OF LENGTH 10
# ---------------------------------------------------------
for i in range(len(s)):
    # Ensure substring length is exactly 10
    if (i + 10) <= len(s):
        key = s[i:i+10]
        dict[key] = dict.get(key, 0) + 1

# ---------------------------------------------------------
# STEP 2: COLLECT SUBSTRINGS WITH FREQUENCY > 1
# ---------------------------------------------------------
for i, j in dict.items():
    if j > 1:
        res.append(i)

# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------
print(res)

# ---------------------------------------------------------
# DRY RUN:
#
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Generated substrings (length = 10):
# "AAAAACCCCC" → appears 2 times
# "CCCCCAAAAA" → appears 2 times
#
# All other substrings appear only once.
#
# Result:
# ["AAAAACCCCC", "CCCCCAAAAA"]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# Generating substrings → O(n)
# Each substring length is constant (10)
# Total → O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ---------------------------------------------------------
