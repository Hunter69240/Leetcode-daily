class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify matrix in-place.
        """

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False   # tracks whether the first row must be zeroed

        # ---------------------------------------------------------
        # EXPLANATION:
        # We use the first row and first column as markers.
        # If matrix[r][c] == 0:
        #     mark its column by setting matrix[0][c] = 0
        #     mark its row by setting matrix[r][0] = 0
        #
        # Special cases:
        # - First row is tracked by 'rowZero'
        # - First column is checked with matrix[0][0]
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # Input:
        # [
        #   [1,1,1],
        #   [1,0,1],
        #   [1,1,1]
        # ]
        #
        # First pass (marking):
        #   r=1, c=1 → matrix[1][1] == 0
        #       matrix[0][1] = 0  (mark column 1)
        #       matrix[1][0] = 0  (mark row 1)
        #
        # Matrix becomes:
        # [
        #   [1,0,1],
        #   [0,0,1],
        #   [1,1,1]
        # ]
        #
        # Second pass (apply markers):
        # For r=1.. end, c=1.. end:
        #   (1,1) ← because matrix[0][1]==0 or matrix[1][0]==0 → becomes 0
        #   (1,2) ← matrix[1][0]==0 → becomes 0
        #   (2,1) ← matrix[0][1]==0 → becomes 0
        #
        # Matrix now:
        # [
        #   [1,0,1],
        #   [0,0,0],
        #   [1,0,1]
        # ]
        #
        # Third: first column?
        # matrix[0][0] != 0 → do nothing
        #
        # Fourth: first row?
        # rowZero == False → do nothing
        #
        # FINAL RESULT:
        # [
        #   [1,0,1],
        #   [0,0,0],
        #   [1,0,1]
        # ]
        # ---------------------------------------------------------

        # ---------------- FIRST PASS: MARK ZEROS ----------------
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0     # mark column
                    if r > 0:
                        matrix[r][0] = 0 # mark row
                    else:
                        rowZero = True   # first row contains a zero

        # ------------- SECOND PASS: ZERO OUT MARKED CELLS -------------
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # ------------- HANDLE FIRST COLUMN IF NEEDED -------------
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # ------------- HANDLE FIRST ROW IF NEEDED -------------
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
