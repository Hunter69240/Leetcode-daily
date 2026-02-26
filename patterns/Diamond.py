'''
Docstring for patterns.Diamond

   *
  ***
 *****
*******
 *****
  ***
   *
'''

# -----------------------------------
# Number of rows (must be odd)
# -----------------------------------
n = 7

# -----------------------------------
# Loop through all rows
# -----------------------------------
for i in range(n):

    # -----------------------------------
    # TOP HALF (including middle row)
    # -----------------------------------
    if i <= n // 2:
        
        # Number of spaces before stars
        spaces = (n // 2) - i
        
        # Number of stars in current row
        stars = 2 * i + 1

        # Print leading spaces
        for j in range(spaces):
            print(" ", end=" ")

        # Print stars
        for k in range(stars):
            print("*", end=" ")

        print()

    # -----------------------------------
    # BOTTOM HALF
    # -----------------------------------
    else:
        
        # Number of spaces increases
        spaces = i - n // 2
        
        # Number of stars decreases
        stars = 2 * (n - i) - 1

        # Print leading spaces
        for j in range(spaces):
            print(" ", end=" ")

        # Print stars
        for k in range(stars):
            print("*", end=" ")

        print()