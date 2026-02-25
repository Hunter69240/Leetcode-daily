# -----------------------------------
# Pyramid Pattern
# -----------------------------------

'''
Expected Output (n = 4)

   *
  ***
 *****
*******
'''

n = 4

for i in range(n):
    
    # Number of spaces before stars
    spaces = n - i - 1
    
    # Number of stars in current row
    stars = 2 * i + 1
    
    # Print left spaces
    for j in range(spaces):
        print(" ", end="")
    
    # Print stars
    for k in range(stars):
        print("*", end="")
    
    # Print right spaces (optional for symmetry)
    for j in range(spaces):
        print(" ", end="")
    
    # Move to next line
    print()