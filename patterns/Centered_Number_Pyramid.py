'''
Docstring for patterns.Centered_Number_Pyramid

   1
  121
 12321
1234321
'''

n = 4

for i in range(1, n + 1):

    # spaces
    for s in range(n - i):
        print(" ", end="")

    # increasing numbers
    for inc in range(1, i + 1):
        print(inc, end="")

    # decreasing numbers
    for dec in range(i - 1, 0, -1):
        print(dec, end="")

    print()