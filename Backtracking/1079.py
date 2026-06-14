tiles = "AAABBC"

# Build frequency map manually
freq = {}
for ch in tiles:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
def backtrack():
    total = 0

    for ch in freq:

        if freq[ch] == 0:
            continue

        total += 1

        freq[ch] -= 1

        total += backtrack()

        freq[ch] += 1

    return total


print(backtrack())


# ------------------------------------------------------------
# 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
# ------------------------------------------------------------
# We are counting all possible non-empty sequences
# that can be formed using the given tiles.
#
# Example:
#
# tiles = "AAB"
#
# Possible sequences:
#
# A
# B
# AA
# AB
# BA
# AAB
# ABA
# BAA
#
# Answer = 8
#
# We do NOT need to generate permutations of fixed length.
#
# We count every possible sequence of every length.


# ------------------------------------------------------------
# 🔹 WHAT TYPE OF PROBLEM IS THIS?
# ------------------------------------------------------------
# This is a BACKTRACKING problem.
#
# Let’s verify using the 3 key questions:
#
# 1. Does it ask for ALL solutions?
#    ✅ Yes → all possible sequences
#
# 2. Do we build the answer piece by piece?
#    ✅ Yes → one character at a time
#
# 3. Can a choice affect future choices?
#    ✅ Yes → using a tile reduces remaining tiles
#
# 👉 Hence: BACKTRACKING


# ------------------------------------------------------------
# 🔹 WHY USE A FREQUENCY MAP?
# ------------------------------------------------------------
#
# freq stores how many copies of each character
# are still available.
#
# Example:
#
# tiles = "AAABBC"
#
# freq =
#
# {
#   'A': 3,
#   'B': 2,
#   'C': 1
# }
#
# Instead of storing positions,
# we store remaining counts.
#
# This automatically avoids duplicate work.


# ------------------------------------------------------------
# 🔹 FUNCTION PURPOSE
# ------------------------------------------------------------
#
# backtrack()
#
# Returns:
#
# Number of sequences that can be formed
# from the currently available tiles.
#
# At every call:
#
# Choose a tile
# →
# Count the newly formed sequence
# →
# Continue extending it


# ------------------------------------------------------------
# 🔹 WHY total = 0 ?
# ------------------------------------------------------------
#
# total stores the number of valid sequences
# found from the current state.
#
# Every recursive call computes its own answer
# and returns it to its parent.


# ------------------------------------------------------------
# 🔹 LOOP OVER ALL CHARACTERS
# ------------------------------------------------------------
#
# for ch in freq:
#
# Try using every available character.
#
# Example:
#
# freq =
#
# {
#   A: 2,
#   B: 1,
#   C: 1
# }
#
# Possible choices:
#
# A
# B
# C


# ------------------------------------------------------------
# 🔹 SKIP UNAVAILABLE CHARACTERS
# ------------------------------------------------------------
#
# if freq[ch] == 0:
#     continue
#
# Example:
#
# freq =
#
# {
#   A: 0,
#   B: 2,
#   C: 1
# }
#
# Cannot choose A anymore.
#
# Skip it.


# ------------------------------------------------------------
# 🔹 WHY total += 1 ?
# ------------------------------------------------------------
#
# Choosing a character immediately creates
# one new valid sequence.
#
# Example:
#
# Current sequence:
#
# ""
#
# Choose A
#
# New sequence:
#
# "A"
#
# Count it.
#
# total += 1
#
#
# Later:
#
# Current sequence:
#
# "AA"
#
# Choose B
#
# New sequence:
#
# "AAB"
#
# Count it.
#
# total += 1
#
#
# Every choice creates exactly one new sequence.


# ------------------------------------------------------------
# 🔹 CHOOSE STEP
# ------------------------------------------------------------
#
# freq[ch] -= 1
#
# Use one copy of the chosen character.
#
# Example:
#
# Before:
#
# A:3
#
# After choosing A:
#
# A:2
#
# Remaining tiles decrease.


# ------------------------------------------------------------
# 🔹 EXPLORE STEP
# ------------------------------------------------------------
#
# total += backtrack()
#
# After creating a sequence,
# try extending it further.
#
# Example:
#
# Current sequence:
#
# A
#
# Recursive calls explore:
#
# AA
# AB
# AC
#
# and all longer sequences starting from A.


# ------------------------------------------------------------
# 🔹 BACKTRACK STEP
# ------------------------------------------------------------
#
# freq[ch] += 1
#
# Restore the tile.
#
# Example:
#
# Before choosing:
#
# A:3
#
# After choosing:
#
# A:2
#
# After backtracking:
#
# A:3
#
# State is restored for the next branch.


# ------------------------------------------------------------
# 🔹 RECURSION TREE (AAB)
# ------------------------------------------------------------
#
# Start
#
# ├── A
# │   ├── A
# │   │   └── B
# │   │
# │   └── B
# │       └── A
# │
# └── B
#     └── A
#         └── A
#
#
# Sequences:
#
# A
# AA
# AAB
# AB
# ABA
# B
# BA
# BAA


# ------------------------------------------------------------
# 🔹 DRY RUN (AAABBC)
# ------------------------------------------------------------
#
# freq =
#
# {
#   A:3,
#   B:2,
#   C:1
# }
#
#
# Choose A
#
# Count:
#
# A
#
# Remaining:
#
# A:2 B:2 C:1
#
#
# Choose A again
#
# Count:
#
# AA
#
#
# Choose A again
#
# Count:
#
# AAA
#
#
# Choose B
#
# Count:
#
# AAAB
#
#
# Choose B
#
# Count:
#
# AAABB
#
#
# Choose C
#
# Count:
#
# AAABBC
#
#
# Backtrack and explore:
#
# AAABC
# AAB
# AABC
# AAC
# AB
# ABA
# ...
#
#
# Then start with:
#
# B
#
# Then:
#
# C
#
#
# Every possible sequence is counted exactly once.


# ------------------------------------------------------------
# 🔹 WHY NO DUPLICATES?
# ------------------------------------------------------------
#
# Frequency map treats identical letters
# as one choice with a count.
#
# Example:
#
# AAA
#
# We do NOT separately choose:
#
# A(1)
# A(2)
# A(3)
#
# We simply choose:
#
# A
#
# and reduce its count.
#
# Therefore duplicate sequences
# are never generated.


# ------------------------------------------------------------
# ✅ FINAL ANSWER
# ------------------------------------------------------------
#
# tiles = "AAABBC"
#
# Total unique sequences = 188
# ------------------------------------------------------------