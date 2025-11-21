'''
1
1 1
1 1 2
1 1 2 3
1 1 2 3 5
'''


rows = 5  # Number of rows in the pattern

# Step 1: Generate Fibonacci numbers up to 'rows'
fib = [1, 1]  # Starting two Fibonacci numbers

# Build Fibonacci list with enough values for the pattern
for i in range(2, rows):
    fib.append(fib[i - 1] + fib[i - 2])  # Standard Fibonacci formula


# Step 2: Build and print each row of the pattern
for i in range(1, rows + 1):  # Loop from 1 to 5 (inclusive)
    line = []  # Temporary list to store numbers for the current row

    for j in range(1, i + 1):  # Print i elements in row i
        if j <= 2:
            line.append(1)  # First two elements are always 1
        else:
            line.append(fib[j - 1])  # Append j-th Fibonacci number

    print(*line)  # Print the row values separated by spaces


