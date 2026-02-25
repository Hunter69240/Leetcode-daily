# -----------------------------------
# Hollow Square Pattern
# -----------------------------------

'''
Expected Output (n = 5)

*****
*   *
*   *
*   *
*****
'''

n = 5

for i in range(n):
    for j in range(n):
        
        # Print * on:
        # 1. First row
        # 2. Last row
        # 3. First column
        # 4. Last column
        if (i == 0 or i == n-1 or j == 0 or j == n-1):
            print("*", end="")
        else:
            print(" ", end="")
    
    # Move to next line after each row
    print()