'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

rows = 5

# Top half
for i in range(rows):  # i goes from 0 to 4 (5 rows)
    
    # Print leading spaces to center the stars
    for j in range(rows - i - 1):
        print(" ", end="")  # Print space without newline

    # Print stars: count = (2 * i + 1)
    for k in range(2 * i + 1):
        print("*", end="")  # Print star without newline

    # Move to the next line after each row
    print()


# Bottom half
for i in range(rows - 2, -1, -1):  # i goes from 3 to 0 (4 rows)

    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")  # Print space without newline

    # Print stars: count = (2 * i + 1)
    for k in range(2 * i + 1):
        print("*", end="")  # Print star without newline

    # Move to the next line
    print()

