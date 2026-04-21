def a():
    # PROBLEM:
    # Build Pascal's Triangle up to numRows.
    # Rule: each element = sum of two elements directly above it.

    numRows = 5

    # BASE CASE:
    # If only one row → triangle = [[1]]
    if numRows == 1:
        return [[1]]

    # DP DEFINITION:
    # res[i] = i-th row of Pascal's Triangle
    # Each row depends only on previous row → DP (state transition)

    # INITIAL STATES:
    # Row 1 → [1]
    # Row 2 → [1,1]
    res = [[1], [1, 1]]

    # DRY RUN START:
    # res = [[1], [1,1]]

    # LOOP TO BUILD ROWS 3 → numRows
    for i in range(3, numRows + 1):

        # Create new row filled with 1s (edges always 1)
        inter_res = [1 for j in range(i)]

        # DRY RUN (i = 3):
        # inter_res = [1,1,1]

        # Get previous row
        prev = res[-1]

        # DRY RUN (i = 3):
        # prev = [1,1]

        # Fill middle values using recurrence
        for j in range(1, len(inter_res) - 1):
            inter_res[j] = prev[j - 1] + prev[j]

            # DRY RUN (i = 3, j = 1):
            # inter_res[1] = prev[0] + prev[1] = 1 + 1 = 2
            # inter_res = [1,2,1]

        # Append new row
        res.append(inter_res)

        # DRY RUN AFTER i = 3:
        # res = [[1], [1,1], [1,2,1]]

        # -----------------------------

        # DRY RUN (i = 4):
        # inter_res = [1,1,1,1]
        # prev = [1,2,1]

        # j = 1:
        # inter_res[1] = 1 + 2 = 3
        # j = 2:
        # inter_res[2] = 2 + 1 = 3
        # inter_res = [1,3,3,1]

        # res = [[1], [1,1], [1,2,1], [1,3,3,1]]

        # -----------------------------

        # DRY RUN (i = 5):
        # inter_res = [1,1,1,1,1]
        # prev = [1,3,3,1]

        # j = 1:
        # inter_res[1] = 1 + 3 = 4
        # j = 2:
        # inter_res[2] = 3 + 3 = 6
        # j = 3:
        # inter_res[3] = 3 + 1 = 4
        # inter_res = [1,4,6,4,1]

        # res = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

    # FINAL RESULT:
    return res


print(a())