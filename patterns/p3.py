'''
     1
    121
   12321
  1234321
 123454321
'''

rows = 5  # Total number of rows for the pyramid

# Outer loop to control the number of rows
for i in range(1, rows + 1):

    # Step 1: Print leading spaces to center the numbers
    for j in range(rows - i):
        print(" ", end=" ")  # One space followed by another to keep pyramid shape

    # Step 2: Print increasing numbers from 1 to i
    for k in range(1, i + 1):
        print(k, end=" ")  # Print number followed by space

    # Step 3: Print decreasing numbers from i-1 down to 1
    for k in range(i - 1, 0, -1):
        print(k, end=" ")  # Print number followed by space

    # Step 4: Move to the next line after each row
    print()

