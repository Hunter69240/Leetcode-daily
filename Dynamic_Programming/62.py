def a():
    # Problem:
    # Count number of unique ways to go from (0,0) to (m-1,n-1)
    # moving only right or down

    m = 3
    n = 7

    # dp[i][j] = number of ways to reach cell (i, j)
    dp = [[0] * n for _ in range(m)]

    # Base: first column → only down moves
    for i in range(m):
        dp[i][0] = 1

    # Base: first row → only right moves
    for j in range(n):
        dp[0][j] = 1

    # Fill remaining cells
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


# --- DRY RUN (m = 3, n = 7) ---

# Initial dp:
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0

# After base initialization:
# 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0
# 1 0 0 0 0 0 0

# Filling:

# i = 1:
# dp[1][1] = 1 + 1 = 2
# dp[1][2] = 1 + 2 = 3
# dp[1][3] = 1 + 3 = 4
# dp[1][4] = 1 + 4 = 5
# dp[1][5] = 1 + 5 = 6
# dp[1][6] = 1 + 6 = 7

# dp now:
# 1 1 1 1 1 1 1
# 1 2 3 4 5 6 7
# 1 0 0 0 0 0 0

# i = 2:
# dp[2][1] = 2 + 1 = 3
# dp[2][2] = 3 + 3 = 6
# dp[2][3] = 4 + 6 = 10
# dp[2][4] = 5 + 10 = 15
# dp[2][5] = 6 + 15 = 21
# dp[2][6] = 7 + 21 = 28

# Final dp:
# 1  1  1  1  1  1  1
# 1  2  3  4  5  6  7
# 1  3  6 10 15 21 28

# Output = 28

print(a())


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # Each cell in 'row' represents the number of ways to reach that cell
#         # from the bottom row. Initialize the last row with all 1's because
#         # there is only one way to move along the bottom row (all right moves).
#         row = [1] * n

#         # Build the DP table from the second-last row up to the top.
#         for i in range(m - 1):
#             # For the new row, the last column is always 1 (only downward moves)
#             newRow = [1] * n

#             # Fill the row from right to left (excluding last column)
#             for j in range(n - 2, -1, -1):
#                 # Number of ways to reach current cell =
#                 # ways from the right + ways from below.
#                 newRow[j] = newRow[j + 1] + row[j]

#             # Move upward: new row becomes the current row
#             row = newRow

#         # The answer is the number of ways to reach the top-left cell
#         return row[0]
