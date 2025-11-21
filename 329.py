class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Memoization dictionary:
        # dp[(r,c)] = length of the longest increasing path starting at (r,c)
        dp = {}

        # Depth-first search function
        def dfs(r, c, prevVal):
            """
            Returns the longest increasing path starting from (r, c),
            only if matrix[r][c] > prevVal.
            """
            # Boundary check AND increasing condition check
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
                matrix[r][c] <= prevVal):
                return 0

            # If we already computed this cell, return memoized result
            if (r, c) in dp:
                return dp[(r, c)]

            # At minimum, the path length is 1 (starting at this cell)
            res = 1

            # Explore four directions:
            # Only move if next cell has strictly greater value
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))  # Down
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))  # Up
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))  # Right
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))  # Left

            # Save result so future searches can reuse it (memoization)
            dp[(r, c)] = res
            return res

        # Run DFS from every cell in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)   # Use -1 so any cell is greater than prevVal

        # Return the longest path found
        return max(dp.values())
