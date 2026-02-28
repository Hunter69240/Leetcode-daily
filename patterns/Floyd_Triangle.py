'''
Docstring for patterns.Floyd's_Triangle

1
2 3
4 5 6
7 8 9 10
'''

n = 4
num = 1   # Starting number

for i in range(1, n + 1):          # Controls number of rows
    for j in range(i):             # Prints i numbers in each row
        print(num, end=" ")
        num += 1                   # Increment number after printing
    print()                        # Move to next line