'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

# Number of rows in the pyramid
rows = 5

# Outer loop to handle the number of rows (from 1 to 5)
for i in range(1, rows + 1):

    # Inner loop to print leading spaces before the stars
    # This creates the pyramid shape by pushing stars to the right
    for j in range(rows - i):
        print(" ", end="")  # Print a space without moving to the next line

    # Inner loop to print stars with a space after each star
    # The number of stars in each row equals the row number
    for j in range(i):
        print("* ", end="")  # Print star followed by a space

    # Move to the next line after each row is printed
    print()