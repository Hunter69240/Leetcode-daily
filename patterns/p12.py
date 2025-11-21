'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''


n = 5
for i in range(1, n + 1):
    # Print leading spaces
    for s in range(n - i):
        print(" ", end=" ")

    # Increasing part: from i to i + (i - 1)
    for j in range(i, i + i - 1):
        print(j, end=" ")

    # Decreasing part: from peak-1 back to i
    for j in range(i + i - 3, i - 1, -1):
        print(j, end=" ")

    print()





