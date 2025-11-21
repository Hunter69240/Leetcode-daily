'''
*****
****
***
**
*

'''

# Number of rows for the inverted left-aligned triangle
rows = 5

# Outer loop: starts from 'rows' and counts down to 1
for i in range(rows, 0, -1):

    # Inner loop to print stars
    # Number of stars printed equals the current row number 'i'
    for j in range(i):
        print("*", end="")  # Print star without newline

    # Move to the next line after each row is printed
    print()
