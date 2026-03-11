class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # board dimensions
        path = set()  # keeps track of visited cells in the current DFS path

        def dfs(r, c, i):
            # Base case: if we've matched all characters in word
            if i == len(word):
                return True

            # Boundary checks:
            # - r, c must be within grid
            # - board[r][c] must match current word[i]
            # - cell (r,c) must not be visited in this path
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore all 4 directions: down, up, right, left
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Backtrack: unmark the cell (so it can be used in another path)
            path.remove((r, c))

            return res

        # Try to start DFS from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # start search if first char matches
                    return True

        # If no path found, word doesn't exist
        return False
