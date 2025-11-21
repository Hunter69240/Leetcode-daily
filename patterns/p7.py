'''
*****
 ****
  ***
   **
    *

'''

# Number of rows for the inverted right-aligned triangle
rows = 5

# Outer loop: starts from 'rows' and decreases to 1
for i in range(rows, 0, -1):

    # Inner loop to print leading spaces
    # Spaces increase as 'i' decreases, to shift the stars to the right
    for j in range(rows - i):
        print(" ", end="")  # Print space without newline

    # Inner loop to print stars
    # Number of stars in each row is equal to 'i'
    for j in range(i):
        print("*", end="")  # Print star without newline

    # Move to the next line after each row
    print()
