class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to keep track of which columns and diagonals are already attacked by queens
        col = set()        # columns where queens are placed
        posDiag = set()    # positive diagonals (r + c) → "\" shaped
        negDiag = set()    # negative diagonals (r - c) → "/" shaped

        res = []  # final result to store all valid board configurations
        # Initialize the chessboard with "." (empty cells)
        board = [["."] * n for i in range(n)]

        # Backtracking function: place queens row by row
        def backtrack(r):
            # Base case: if all n queens are placed, save current board configuration
            if r == n:
                copy = ["".join(row) for row in board]  # convert board rows to strings
                res.append(copy)
                return 
            
            # Try placing a queen in each column of the current row
            for c in range(n):
                # If the column or diagonals are already under attack, skip this cell
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place the queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to the next row
                backtrack(r + 1)

                # Backtrack: remove the queen and reset state
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start the recursion from the first row
        backtrack(0)

        return res
