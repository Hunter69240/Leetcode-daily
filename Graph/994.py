from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Queue for BFS (stores positions of rotten oranges)
        q = deque()

        # 'time' counts minutes passed, 'fresh' counts fresh oranges
        time, fresh = 0, 0

        # Dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Step 1: Count fresh oranges and enqueue rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1   # count fresh orange
                if grid[r][c] == 2:
                    q.append([r, c])  # rotten orange goes into queue

        # Possible 4 directions (up, down, left, right)
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # Step 2: BFS traversal - spread rot level by level
        while q and fresh > 0:  
            # Process all currently rotten oranges in this minute
            for i in range(len(q)):
                r, c = q.popleft()

                # Check all 4 directions
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Skip if out of bounds or not a fresh orange
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue

                    # Mark fresh orange as rotten
                    grid[row][col] = 2
                    # Add this newly rotten orange to queue
                    q.append([row, col])
                    # Decrease fresh count
                    fresh -= 1

            # After processing one "minute" of spread
            time += 1

        # Step 3: If no fresh oranges left, return time, else -1
        return time if fresh == 0 else -1
