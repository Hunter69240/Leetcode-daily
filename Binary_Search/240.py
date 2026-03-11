def a():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5

    i = 0                      # start from first row
    j = len(matrix[0]) - 1     # start from last column (top-right corner)

    while i <= len(matrix) - 1 and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1             # move left
        else:
            i += 1             # move down

    return False


c = a()
print(c)


# ---------------------------------------------------------
# EXPLANATION:
# This code searches for a target in a 2D matrix where:
# - Each row is sorted left to right
# - Each column is sorted top to bottom
#
# This is the "Search a 2D Matrix II" problem.
#
# STRATEGY (Greedy):
# - Start from the TOP-RIGHT corner
#
# Why top-right?
# - Left side has smaller values
# - Down side has larger values
#
# At any cell:
# - If value > target → move LEFT
# - If value < target → move DOWN
#
# This guarantees we eliminate one row or one column
# in every step.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY THIS WORKS:
#
# At position (i, j):
# - All elements LEFT of it are smaller
# - All elements BELOW it are larger
#
# So:
# - If current > target → target cannot be below → go left
# - If current < target → target cannot be left → go down
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# matrix =
# [
#  [ 1,  4,  7, 11, 15],
#  [ 2,  5,  8, 12, 19],
#  [ 3,  6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
# ]
# target = 5
#
# Start at top-right:
# i=0, j=4 → matrix[0][4]=15
# 15 > 5 → move LEFT → j=3
#
# i=0, j=3 → 11
# 11 > 5 → move LEFT → j=2
#
# i=0, j=2 → 7
# 7 > 5 → move LEFT → j=1
#
# i=0, j=1 → 4
# 4 < 5 → move DOWN → i=1
#
# i=1, j=1 → 5
# 5 == target → FOUND → return True
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(m + n)
# m = number of rows
# n = number of columns
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
