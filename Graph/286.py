class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Get dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        visit = set()     # To keep track of visited cells
        q = deque()       # Queue for BFS
        
        # Helper function to add a valid room (cell) into the queue
        def addRoom(r, c):
            # Out of bounds OR already visited OR it's a wall (-1) → skip
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                (r, c) in visit or 
                grid[r][c] == -1):
                return
            # Otherwise mark visited and add to queue
            visit.add((r, c))
            q.append([r, c])
        
        # Step 1: Add all "treasure rooms" (cells with 0) to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
    
        # Step 2: Multi-source BFS from all treasures
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # Update distance from nearest treasure
                
                # Explore neighbors (up, down, left, right)
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            dist += 1
