def s():
    # Input string and number of rows
    s = "PAYPALISHIRING"
    numRows = 3

    # Dictionary to store characters for each row
    d = {}

    # Direction of movement:
    #  1  → moving down (towards increasing row index)
    # -1  → moving up   (towards decreasing row index)
    direction = 1

    # Current row pointer (starts from top row)
    j = 0

    # Initialize all rows with empty strings
    for i in range(numRows):
        d[i] = ""

    # ---------------------------------------------------------
    # DERIVATION OF ZIGZAG CYCLE LENGTH
    #
    # Zigzag movement consists of:
    # 1) Moving DOWN from row 0 to row (numRows - 1)
    #    → this takes (numRows - 1) steps
    #
    # 2) Moving UP from row (numRows - 1) back to row 0
    #    → this also takes (numRows - 1) steps
    #
    # Therefore, one full zigzag "bounce" takes:
    # (numRows - 1) + (numRows - 1) = 2 * (numRows - 1) steps
    #
    # Each character advances the pointer by one step,
    # so after this many characters, the zigzag pattern repeats.
    # ---------------------------------------------------------
    cycle = 2 * (numRows - 1)

    # Edge case: when there is only one row,
    # no zigzag is possible; return the original string
    if cycle == 0:
        return s

    # Traverse each character in the string
    for i in range(len(s)):
        # index represents the current position
        # within one full zigzag cycle
        index = i % cycle

        # If we are at the top row (start of a cycle),
        # we must start moving downward
        if index == 0:
            direction = 1

        # If we are at the bottom row,
        # we must reverse direction and move upward
        elif index == numRows - 1:
            direction = -1

        # Append the current character to the current row
        d[j] += s[i]

        # Move to the next row according to the direction
        j += direction

    # Combine all rows to get the final zigzag string
    print("".join(list(d.values())))
