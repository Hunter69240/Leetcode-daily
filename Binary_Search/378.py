def kthSmallest(matrix, k):
    n = len(matrix)

    # value range (smallest to largest element in matrix)
    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    # binary search on VALUE space
    while low <= high:
        mid = (low + high) // 2

        count = count_less_equal(matrix, mid)

        if count < k:
            low = mid + 1
        else:
            high = mid - 1

    return low


def count_less_equal(matrix, x):
    n = len(matrix)
    row = n - 1    # start from bottom-left
    col = 0
    count = 0

    while row >= 0 and col < n:
        if matrix[row][col] <= x:
            # all values above (0..row) in this column are <= x
            count += row + 1
            col += 1
        else:
            # current value too large, move up
            row -= 1

    return count


# ---------------------------------------------------------
# EXPLANATION:
# This code finds the K-th SMALLEST element in a SORTED MATRIX.
#
# Matrix properties:
# - Each row is sorted in ascending order
# - Each column is sorted in ascending order
#
# IMPORTANT:
# We do NOT flatten the matrix.
# Instead, we binary-search on the VALUE RANGE.
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY IDEA:
#
# If we can count how many numbers in the matrix are
# <= some value `x`, then we can binary search for the
# smallest value whose count >= k.
#
# This is a classic "binary search on answer" problem.
# ---------------------------------------------------------

# ---------------------------------------------------------
# OUTER BINARY SEARCH (kthSmallest):
#
# low  = smallest value in matrix
# high = largest value in matrix
#
# mid = candidate value
#
# If count(mid) < k:
#   → kth smallest is larger → move right
#
# Else:
#   → kth smallest is <= mid → move left
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW count_less_equal WORKS:
#
# Start from BOTTOM-LEFT corner.
#
# Why bottom-left?
# - Moving RIGHT increases values
# - Moving UP decreases values
#
# At position (row, col):
# - If matrix[row][col] <= x:
#     all values above it in that column are also <= x
#     → add (row + 1) to count
#     → move RIGHT
#
# - Else:
#     value too big
#     → move UP
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# matrix =
# [
#  [ 1,  5,  9],
#  [10, 11, 13],
#  [12, 13, 15]
# ]
# k = 8
#
# VALUE RANGE:
# low=1, high=15
#
# mid=8
# count <= 8 = 2 (1,5)
# < k → move right → low=9
#
# mid=12
# count <= 12 = 6
# < k → move right → low=13
#
# mid=14
# count <= 14 = 8
# >= k → move left → high=13
#
# mid=13
# count <= 13 = 8
# >= k → move left → high=12
#
# loop ends → low=13
#
# FINAL ANSWER:
# 13
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n log (max - min))
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
