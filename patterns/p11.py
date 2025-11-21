'''
        1
      2 3
    3 4 5
  4 5 6 7
5 6 7 8 9   
'''
n = 5  # Number of rows

for i in range(1, n + 1):  # i from 1 to 5 (row number)

    # Print leading spaces to center the pyramid
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    # Print increasing numbers starting from i
    num = i  # Starting number for this row
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1  # Move to next number

    print()  # Move to next line


    