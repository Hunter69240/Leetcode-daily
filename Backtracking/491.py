nums = [4, 6, 7, 7]
res = []

def backtracking(cur, index):

    if len(cur) >= 2:
        res.append(cur[:])

    s = set()

    for i in range(index, len(nums)):

        if nums[i] in s:
            continue

        elif cur and nums[i] < cur[-1]:
            continue

        else:
            s.add(nums[i])

            cur.append(nums[i])

            backtracking(cur, i + 1)

            cur.pop()

backtracking([], 0)

print(res)


# ------------------------------------------------------------
# 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
# ------------------------------------------------------------
# We are finding all increasing subsequences of length ≥ 2.
#
# A subsequence:
# - Does NOT need to be contiguous
# - Must maintain original order
#
# Condition:
# - Sequence must be NON-DECREASING (nums[i] >= previous element)
#
# So this is NOT a numerical sum problem,
# but a problem where we COLLECT all valid subsequences.


# ------------------------------------------------------------
# 🔹 WHAT TYPE OF PROBLEM IS THIS?
# ------------------------------------------------------------
# This is a BACKTRACKING problem.
#
# Let’s verify using the 3 key questions:
#
# 1. Does it ask for ALL solutions?
#    ✅ Yes → we need ALL increasing subsequences
#
# 2. Do you build the answer piece by piece?
#    ✅ Yes → we keep adding elements to current sequence (cur)
#
# 3. Can a partial solution become invalid mid-way?
#    ✅ Yes → if next number < last element → invalid → skip
#
# 👉 Hence: BACKTRACKING


# ------------------------------------------------------------
# 🔹 FUNCTION PARAMETERS
# ------------------------------------------------------------
#
# cur
# Current subsequence being built.
#
# index
# Starting position from where we can choose next element.
#
# Example:
#
# nums = [4,6,7,7]
#
# cur = [4,6]
# index = 2
#
# Means:
# We have already picked 4 and 6.
# Now we may only choose from:
#
# [7,7]
#  ^
# index = 2


# ------------------------------------------------------------
# 🔹 BASE CASE
# ------------------------------------------------------------
#
# if len(cur) >= 2:
#     res.append(cur[:])
#
# Any subsequence of length ≥ 2 is valid.
#
# We copy using cur[:] because cur is modified later
# during backtracking.


# ------------------------------------------------------------
# 🔹 WHY THE SET?
# ------------------------------------------------------------
#
# s = set()
#
# Used to prevent duplicate subsequences.
#
# Example:
#
# nums = [4,6,7,7]
#
# From:
#
# cur = [4]
#
# We can choose:
#
# first 7  -> [4,7]
# second 7 -> [4,7]
#
# Same subsequence generated twice.
#
# The set ensures that at ONE recursion level
# a value is used only once.
#
# Important:
#
# It does NOT prevent:
#
# [7,7]
#
# because deeper recursive calls create a NEW set.


# ------------------------------------------------------------
# 🔹 VALIDATION CHECK
# ------------------------------------------------------------
#
# elif cur and nums[i] < cur[-1]:
#
# Current number is smaller than the last selected number.
#
# Example:
#
# cur = [4,6]
#
# next = 5
#
# Gives:
#
# [4,6,5]
#
# which is not non-decreasing.
#
# Therefore skip.


# ------------------------------------------------------------
# 🔹 CHOOSE → EXPLORE → UNDO
# ------------------------------------------------------------
#
# cur.append(nums[i])
#
# Choose current number.
#
# backtracking(cur, i + 1)
#
# Explore all possibilities after choosing it.
#
# cur.pop()
#
# Undo choice so we can try the next option.
#
# This pattern is the heart of backtracking.


# ------------------------------------------------------------
# 🔹 DRY RUN (nums = [4,6,7,7])
# ------------------------------------------------------------
#
# backtracking([],0)
#
# ├── 4
# │   ├── 6
# │   │   ├── 7
# │   │   │   └── 7
# │   │   └── 7
# │   └── 7
# │       └── 7
# ├── 6
# │   └── 7
# │       └── 7
# └── 7
#     └── 7
#
# Valid subsequences collected:
#
# [4,6]
# [4,6,7]
# [4,6,7,7]
# [4,7]
# [4,7,7]
# [6,7]
# [6,7,7]
# [7,7]


# ------------------------------------------------------------
# ✅ FINAL OUTPUT
# ------------------------------------------------------------
#
# [
#   [4,6],
#   [4,6,7],
#   [4,6,7,7],
#   [4,7],
#   [4,7,7],
#   [6,7],
#   [6,7,7],
#   [7,7]
# ]