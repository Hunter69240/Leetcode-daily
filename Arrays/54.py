class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # ---------------------------------------------------------
        # EXPLANATION:
        # We traverse the matrix in spiral order using boundaries:
        #   left   → left column index
        #   right  → one past right column index
        #   top    → top row index
        #   bottom → one past bottom row index
        #
        # In each loop, we:
        #   1) Traverse top row (left → right)
        #   2) Traverse right column (top → bottom)
        #   3) Traverse bottom row (right → left)
        #   4) Traverse left column (bottom → top)
        #
        # After each traversal, we shrink the boundaries inward.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # matrix =
        # [
        #   [1, 2, 3],
        #   [4, 5, 6],
        #   [7, 8, 9]
        # ]
        #
        # Initial:
        # left=0, right=3, top=0, bottom=3
        #
        # Top row (row 0):
        #   append 1,2,3
        #   res = [1,2,3]
        #   top = 1
        #
        # Right column (col 2):
        #   append 6,9
        #   res = [1,2,3,6,9]
        #   right = 2
        #
        # Bottom row (row 2):
        #   append 8,7
        #   res = [1,2,3,6,9,8,7]
        #   bottom = 2
        #
        # Left column (col 0):
        #   append 4
        #   res = [1,2,3,6,9,8,7,4]
        #   left = 1
        #
        # Loop continues but left >= right or top >= bottom → stop
        #
        # Final result:
        # res = [1,2,3,6,9,8,7,4]
        # ---------------------------------------------------------

        while left < right and top < bottom:

            # Traverse top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if boundaries are still valid
            if not (left < right and top < bottom):
                break

            # Traverse bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
