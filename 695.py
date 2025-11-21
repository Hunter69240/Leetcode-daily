class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()   # keeps track of visited cells

        # DFS returns the size (area) of the island starting at (r, c)
        def dfs(r, c):
            # base cases: out of bounds, water, or already visited
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                grid[r][c] == 0 or 
                (r, c) in visit):
                return 0

            # mark this land cell as visited
            visit.add((r, c))

            # explore in 4 directions (down, up, right, left)
            return (1 + dfs(r+1, c) +  # down
                      dfs(r-1, c) +    # up
                      dfs(r, c+1) +    # right
                      dfs(r, c-1))     # left

        area = 0
        # check every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # run DFS if this is land and not visited
                area = max(area, dfs(r, c))

        return area  # max area of any island found
