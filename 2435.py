class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # 3-D DP cache:
        # cache[r][c][mod] = number of valid paths starting from (r, c)
        # where current sum % k == mod
        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]
        
        MOD = 10**9 + 7  # requirement for large modulo
        
        def dfs(r, c, remain):
            """
            r, c  : current cell
            remain: current prefix sum modulo k so far
            return: number of valid paths from (r, c) to bottom-right
            """

            # If we reach bottom-right cell, check if final modulo becomes 0
            if r == ROWS - 1 and c == COLS - 1:
                remain = (remain + grid[r][c]) % k
                return 0 if remain else 1  # return 1 only if divisible by k

            # If outside the grid → no path
            if r == ROWS or c == COLS:
                return 0

            # Use memoized result if available
            if cache[r][c][remain] > -1:
                return cache[r][c][remain]

            # Update modulo after adding current cell
            new_mod = (remain + grid[r][c]) % k

            # Move down or right
            ways_down = dfs(r + 1, c, new_mod) % MOD
            ways_right = dfs(r, c + 1, new_mod) % MOD

            # Cache and return total paths from this state
            cache[r][c][remain] = (ways_down + ways_right) % MOD
            return cache[r][c][remain]

        return dfs(0, 0, 0)


'''
🔍 What this algorithm does

We count paths from top-left to bottom-right moving only down or right, such that:

sum of all values along path % k == 0


Because we need to include modulo state, this becomes dynamic programming with 3 dimensions:

(r, c, remainder % k)


grid = [
  [5, 2],
  [1, 3]
]
k = 3


Path 1: 5 → 2 → 3 = 10 → 10 % 3 = 1  ❌ not counted
Path 2: 5 → 1 → 3 = 9 → 9 % 3 = 0   ✔ counted


dfs(0,0,0)
  new_mod = (0 + 5) % 3 = 2
  dfs(1,0,2)
      new_mod = (2 + 1) % 3 = 0
      dfs(1,1,0) → match final mod → returns 1
      dfs(1,?) = OOB → 0
      return 1
  dfs(0,1,2)
      new_mod = (2 + 2) % 3 = 1
      dfs(1,1,1) → final mod = (1 + 3) % 3 = 1 → returns 0
      return 0
→ total = 1 + 0 = 1




'''