def a():
    obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    m=len(obstacleGrid)
    n=len(obstacleGrid[0))

    dp=[[0]*n for _ in range(m)]

    dp[0][0]=1 if obstacleGrid[0][0]!=1 else 0
    # Starting cell: if obstacle then 0, else 1 (we are here, 1 way)

    for i in range(1,n):
        dp[0][i] = 1 if (dp[0][i-1]==1 and obstacleGrid[0][i] !=1) else 0
    # First row: only reachable if previous cell was reachable AND current cell has no obstacle
    # Once blocked, everything after becomes 0

    for j in range(1,m):
        dp[j][0] = 1 if (dp[j-1][0]==1 and obstacleGrid[j][0] !=1) else 0
    # First col: only reachable if cell above was reachable AND current cell has no obstacle
    # Once blocked, everything below becomes 0

    for i in range(1,(m)):
        for j in range(1,(n)):
            if obstacleGrid[i][j]==1:
                dp[i][j]=0
                # Obstacle: no path can pass through, force 0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                # Free cell: paths = ways from above + ways from left

    return dp[m-1][n-1]
    # Bottom-right cell = total unique paths

    # ─── DRY RUN ───────────────────────────────────────────
    # obstacleGrid:        dp after init:
    # 0 0 0                1 0 0
    # 0 1 0                0 0 0
    # 0 0 0                0 0 0
    #
    # after first row loop:
    # 1 1 1
    # 0 0 0
    # 0 0 0
    #
    # after first col loop:
    # 1 1 1
    # 1 0 0
    # 1 0 0
    #
    # main loop:
    # i=1,j=1: obstacle! dp[1][1]=0
    # i=1,j=2: dp[0][2]+dp[1][1] = 1+0 = 1
    # i=2,j=1: dp[1][1]+dp[2][0] = 0+1 = 1
    # i=2,j=2: dp[1][2]+dp[2][1] = 1+1 = 2
    #
    # final dp:
    # 1 1 1
    # 1 0 1
    # 1 1 2
    #
    # answer: dp[2][2] = 2 ✅

print(a())