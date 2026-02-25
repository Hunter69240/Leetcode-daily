# -----------------------------------
# Right Aligned Number Triangle
# -----------------------------------

'''
Expected Output (n = 5)

    1
   12
  123
 1234
12345
'''

n = 5

for i in range(1, n+1):
    
    # Number of leading spaces
    spaces = n - i
    
    # Print spaces
    for j in range(spaces):
        print(" ", end="")
    
    # Print numbers from 1 to i
    for k in range(1, i+1):
        print(k, end="")
    
    # Move to next line
    print()