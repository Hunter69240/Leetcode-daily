def a():
    n = 5                     # Given number (example input)

    x = n ^ (n >> 1)          # XOR n with n shifted right by 1
                               # This highlights positions where adjacent bits differ

    # Check if x is of the form 111... (all 1s)
    # Property: For numbers like 1, 3, 7, 15 -> x & (x+1) == 0
    if (x & (x + 1)) == 0:
        return True           # Means n has alternating bits
    else:
        return False          # Not alternating

print(a())
