#This is Pattern 2 (Grid DP) because the problem represents movement through a grid from top-left to bottom-right. Each cell depends on the number of ways to reach the cell above and the cell to the left. The 1D array is only a space-optimized representation of the grid DP table.


def a():
    grid = [[1,2,3],[4,5,6]]

    row = len(grid)
    col = len(grid[0])
    dp = [[0]*col for _ in range(row)]
    # Create 2x3 table of 0s to store minimum path cost to reach each cell

    dp[0][0] = grid[0][0]
    # Starting cell has no previous cells, cost is just itself

    for i in range(1, col):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    # First row: can only come from left, so cumulative sum left to right

    for j in range(1, row):
        dp[j][0] = grid[j][0] + dp[j-1][0]
    # First col: can only come from above, so cumulative sum top to bottom

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    # Robot came from top or left, pick whichever path was cheaper, add current cell cost

    return dp[-1][-1]
    # Bottom-right cell contains minimum cost of entire path from start to end

    # ─── DRY RUN ───────────────────────────────────────────
    # grid:
    # 1 2 3
    # 4 5 6
    #
    # after dp[0][0]:
    # 1 0 0
    # 0 0 0
    #
    # after first row loop:
    # 1 3 6
    # 0 0 0
    #
    # after first col loop:
    # 1 3 6
    # 5 0 0
    #
    # main loop:
    # i=1,j=1: grid[1][1] + min(dp[0][1], dp[1][0]) = 5 + min(3,5) = 8
    # i=1,j=2: grid[1][2] + min(dp[0][2], dp[1][1]) = 6 + min(6,8) = 12
    #
    # final dp:
    # 1  3  6
    # 5  8  12
    #
    # answer: dp[-1][-1] = 12 ✅

print(a())