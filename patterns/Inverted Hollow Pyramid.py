'''
Docstring for patterns.Inverted Hollow Pyramid

*********
 *     *
  *   *
   * *
    *
'''

# -----------------------------------
# Total width (must be odd)
# -----------------------------------
n = 9

# -----------------------------------
# Loop for rows
# We only need (n//2 + 1) rows
# -----------------------------------
for i in range(n // 2 + 1):

    # -----------------------------------
    # Loop for columns (0 → n-1)
    # -----------------------------------
    for j in range(n):

        # -----------------------------------
        # Print '*' in 3 cases:
        #
        # 1. First row (i == 0)
        # 2. Left boundary  (j == i)
        # 3. Right boundary (j == n - i - 1)
        # -----------------------------------
        if i == 0 or j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()