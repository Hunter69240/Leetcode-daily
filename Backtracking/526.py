class Solution:
    def countArrangement(self, n: int) -> int:
        visited = set()
        count = 0
        def backtracking(index):
            nonlocal count
            if index > n:
                count += 1
                return
            for i in range(1, n + 1):

                if i in visited:
                    continue

                if not (i % index == 0 or index % i == 0):
                    continue

                visited.add(i)

                backtracking(index + 1)

                visited.remove(i)

        backtracking(1)

        return count


# ------------------------------------------------------------
# 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
# ------------------------------------------------------------
# We are counting the number of "beautiful arrangements".
#
# A beautiful arrangement is a permutation of numbers from 1 to n
# such that for every position `index` (1-based):
#
#    number % index == 0  OR  index % number == 0
#
# So instead of summing numbers, we are "counting valid permutations".
#
# 👉 This is a COUNTING problem over permutations with constraints.


# ------------------------------------------------------------
# 🔹 WHAT TYPE OF PROBLEM IS THIS?
# ------------------------------------------------------------
# This is a BACKTRACKING problem.
#
# Let’s verify using the 3 key questions:
#
# 1. Does it ask for ALL solutions?
#    ✅ Yes → we must count ALL valid permutations
#
# 2. Do we build the answer piece by piece?
#    ✅ Yes → we fill positions one by one (index = 1 → n)
#
# 3. Can a partial solution become invalid mid-way?
#    ✅ Yes → if condition fails, we abandon and backtrack
#
# 👉 Hence: BACKTRACKING


# ------------------------------------------------------------
# 🔹 VARIABLES INITIALIZATION
# ------------------------------------------------------------
#
# visited = set()
#
# Keeps track of numbers already used in the permutation.
# Ensures each number is used only once.
#
#
# count = 0
#
# Stores total number of valid arrangements found.


# ------------------------------------------------------------
# 🔹 FUNCTION PARAMETERS
# ------------------------------------------------------------
#
# backtracking(index)
#
# index
# Current position we are trying to fill.
#
# Example:
#
# n = 4
#
# index = 3
#
# Means:
# Positions 1 and 2 are already filled.
# We are now deciding which number should be placed
# at position 3.


# ------------------------------------------------------------
# 🔹 BASE CASE
# ------------------------------------------------------------
#
# if index > n:
#
# Means every position from 1 to n has been filled
# successfully.
#
# Therefore we found one beautiful arrangement.
#
# count += 1


# ------------------------------------------------------------
# 🔹 TRY ALL POSSIBLE CHOICES
# ------------------------------------------------------------
#
# for i in range(1, n + 1):
#
# Try every number from 1 to n.
#
# Example:
#
# n = 3
#
# Possible numbers:
#
# 1, 2, 3
#
# For the current position, we check whether
# each number can be placed there.


# ------------------------------------------------------------
# 🔹 VALIDATION CHECK 1
# ------------------------------------------------------------
#
# if i in visited:
#
# Number already used in another position.
#
# Example:
#
# Arrangement so far:
#
# [2, 1, _]
#
# visited = {1,2}
#
# We cannot use 1 or 2 again.
#
# Skip them.


# ------------------------------------------------------------
# 🔹 VALIDATION CHECK 2
# ------------------------------------------------------------
#
# if not (i % index == 0 or index % i == 0):
#
# Beautiful arrangement condition.
#
# At position 'index', number 'i' is allowed only if:
#
# i divides index
#
# OR
#
# index divides i
#
# Example:
#
# index = 2
# i = 4
#
# 4 % 2 == 0
#
# Valid.
#
#
# Example:
#
# index = 3
# i = 2
#
# 2 % 3 != 0
# 3 % 2 != 0
#
# Invalid.
#
# Skip.


# ------------------------------------------------------------
# 🔹 CHOOSE → EXPLORE → UNDO
# ------------------------------------------------------------
#
# visited.add(i)
#
# Choose number i for current position.
#
#
# backtracking(index + 1)
#
# Move to next position.
#
#
# visited.remove(i)
#
# Undo choice so we can try another number.
#
# This is the classic backtracking pattern.


# ------------------------------------------------------------
# 🔹 DRY RUN (n = 2)
# ------------------------------------------------------------
#
# Initial:
#
# visited = {}
# count = 0
#
#
# backtracking(1)
#
# Position 1:
#
# Try 1
# → valid
#
# visited = {1}
#
# backtracking(2)
#
#
# Position 2:
#
# Try 1
# → already used
#
# Try 2
# → valid
#
# visited = {1,2}
#
# backtracking(3)
#
# index > n
#
# count = 1
#
#
# Backtrack to position 1
#
# Try 2
#
# visited = {2}
#
# backtracking(2)
#
#
# Position 2:
#
# Try 1
#
# 2 % 1 == 0
#
# valid
#
# visited = {2,1}
#
# backtracking(3)
#
# index > n
#
# count = 2


# ------------------------------------------------------------
# 🔹 RECURSION TREE (n = 2)
# ------------------------------------------------------------
#
# backtracking(1)
#
# ├── place 1
# │   └── place 2
# │       └── count += 1
# │
# └── place 2
#     └── place 1
#         └── count += 1


# ------------------------------------------------------------
# ✅ FINAL ANSWER
# ------------------------------------------------------------
#
# count = 2
#
# Arrangements:
#
# [1,2]
# [2,1]
#
# Answer = 2
# ------------------------------------------------------------