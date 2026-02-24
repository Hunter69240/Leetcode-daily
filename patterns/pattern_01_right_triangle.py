# '''
# Docstring for patterns.pattern_01_right_triangle

# *
# **
# ***
# ****
# '''

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# '''
# ****
# ***
# **
# *
# '''
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()


# '''
# Docstring for patterns.pattern_01_right_triangle

#    *
#   **
#  ***
# ****
# '''

# n = 4

# for i in range(n):
#     # Print spaces
#     for k in range(n - i - 1):
#         print(" ", end="")
    
#     # Print stars
#     for j in range(i + 1):
#         print("*", end="")
    
#     # Move to next line
#     print()

# '''
# Docstring for patterns.pattern_01_right_triangle
# ****
#  ***
#   **
#    *
# '''

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n-i):
#         print("*",end="")
#     print()

