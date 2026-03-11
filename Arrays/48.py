class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Modify matrix in-place.
        """

        l, r = 0, len(matrix) - 1

        # ---------------------- EXPLANATION + DRY RUN ----------------------
        # We rotate layer by layer. Each layer is bounded by l (left) and r (right).
        #
        # For each layer:
        #   We rotate 4 values at a time:
        #     top-left     ← bottom-left
        #     bottom-left  ← bottom-right
        #     bottom-right ← top-right
        #     top-right    ← saved top-left
        #
        # Loop continues until l crosses r.
        #
        # ---------------------- DRY RUN (3x3 EXAMPLE) ----------------------
        # Initial matrix:
        # [
        #   [1,2,3],
        #   [4,5,6],
        #   [7,8,9]
        # ]
        #
        # l = 0, r = 2
        #
        # -------- i = 0 --------
        # top = 0, bottom = 2
        # topLeft = matrix[0][0] = 1
        #
        # matrix[0][0] ← matrix[2][0]  → 7
        # matrix[2][0] ← matrix[2][2]  → 9
        # matrix[2][2] ← matrix[0][2]  → 3
        # matrix[0][2] ← topLeft       → 1
        #
        # Matrix now:
        # [
        #   [7,2,1],
        #   [4,5,6],
        #   [9,8,3]
        # ]
        #
        # -------- i = 1 --------
        # top = 0, bottom = 2
        # topLeft = matrix[0][1] = 2
        #
        # matrix[0][1] ← matrix[1][0]  → 4
        # matrix[1][0] ← matrix[2][1]  → 8
        # matrix[2][1] ← matrix[1][2]  → 6
        # matrix[1][2] ← topLeft       → 2
        #
        # Matrix now:
        # [
        #   [7,4,1],
        #   [8,5,2],
        #   [9,6,3]
        # ]
        #
        # Now l=1, r=1 → layer complete → stop.
        #
        # Final rotated matrix:
        # [
        #   [7,4,1],
        #   [8,5,2],
        #   [9,6,3]
        # ]
        # -------------------------------------------------------------------

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save top-left
                topLeft = matrix[top][l + i]

                # bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # saved top-left → top-right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1
