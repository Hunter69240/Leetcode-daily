'''
*****
*   *
*   *
*   *
*****
'''
# Ask the user to input the number of rows for the square
rows = int(input("Enter the number of rows: "))

# Outer loop: goes through each row (from 0 to rows - 1)
for i in range(rows):

    # Inner loop: goes through each column (from 0 to rows - 1)
    for j in range(rows):

        # Print '*' for the border of the square
        # i == 0 → top row
        # i == rows - 1 → bottom row
        # j == 0 → leftmost column
        # j == rows - 1 → rightmost column
        if (i == 0 or i == rows - 1 or j == 0 or j == rows - 1):
            print("*", end="")  # Print star without moving to next line

        else:
            print(" ", end="")  # Print space inside the square

    # After each row is complete, move to the next line
    print()
