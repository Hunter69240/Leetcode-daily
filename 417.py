class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        # Dimensions of the matrix
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to record cells that can reach Pacific and Atlantic oceans
        pac, atl = set(), set()

        # DFS helper function
        def dfs(r, c, visit, prevHeight):
            # Stop if:
            # - already visited
            # - out of bounds
            # - current height < previous height (water can't flow uphill)
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return

            # Mark current cell as visited
            visit.add((r, c))

            # Explore all 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Step 1: Run DFS from Pacific Ocean borders (top row & left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])             # top row → Pacific
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c]) # bottom row → Atlantic

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])             # left column → Pacific
            dfs(r, COLS - 1, atl, heights[r][COLS-1]) # right column → Atlantic

        # Step 2: Collect cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
