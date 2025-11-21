class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Each cell in 'row' represents the number of ways to reach that cell
        # from the bottom row. Initialize the last row with all 1's because
        # there is only one way to move along the bottom row (all right moves).
        row = [1] * n

        # Build the DP table from the second-last row up to the top.
        for i in range(m - 1):
            # For the new row, the last column is always 1 (only downward moves)
            newRow = [1] * n

            # Fill the row from right to left (excluding last column)
            for j in range(n - 2, -1, -1):
                # Number of ways to reach current cell =
                # ways from the right + ways from below.
                newRow[j] = newRow[j + 1] + row[j]

            # Move upward: new row becomes the current row
            row = newRow

        # The answer is the number of ways to reach the top-left cell
        return row[0]
