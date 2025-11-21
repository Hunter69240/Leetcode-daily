import collections  # required for deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0  # empty grid -> no islands

        rows, cols = len(grid), len(grid[0])  # dimensions of the grid

        visit = set()   # to track visited cells
        islands = 0     # count of islands found

        # Breadth-first search to explore an island
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))   # mark the starting cell as visited
            q.append((r, c))    # enqueue the starting cell

            while q:
                row, col = q.pop()  # pop from queue (acts like stack here)
                # possible movement directions: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc  # neighbor cell
                    # check boundaries, land cell, and not visited
                    if ((r) in range(rows) and 
                        (c) in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))   # add neighbor to queue
                        visit.add((r, c))  # mark as visited

        # iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # start BFS when we find an unvisited land cell
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1  # each BFS call discovers a new island

        return islands  # total number of islands
