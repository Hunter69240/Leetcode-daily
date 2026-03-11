def findNthDigit(n):
    digit_len = 1
    count = 9
    start = 1

    # Step 1: Find the digit-length group
    while n > digit_len * count:
        n -= digit_len * count
        digit_len += 1
        count *= 10
        start *= 10

    # Step 2: Find the exact number
    number = start + (n - 1) // digit_len

    # Step 3: Find the exact digit
    digit_index = (n - 1) % digit_len
    return int(str(number)[digit_index])


a = findNthDigit(12)
print(a)


# ---------------------------------------------------------
# EXPLANATION:
# This code finds the N-th digit in the infinite sequence:
#
#   "1234567891011121314..."
#
# The digits are formed by concatenating all positive integers.
#
# We DO NOT build the string (too slow).
# Instead, we mathematically locate the digit.
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 1: IDENTIFY THE DIGIT-LENGTH GROUP
#
# Numbers grouped by digit length:
# 1-digit  → 1 to 9      → 9 numbers  → 9 digits
# 2-digit  → 10 to 99    → 90 numbers → 180 digits
# 3-digit  → 100 to 999  → 900 numbers → 2700 digits
#
# We subtract whole groups until n lies inside one group.
# ---------------------------------------------------------

# ---------------------------------------------------------
# VARIABLES:
#
# digit_len → number of digits per number in current group
# count     → how many numbers in this group
# start     → first number in this group
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (n = 12):
#
# Initial:
# n = 12
# digit_len = 1
# count = 9
# start = 1
#
# Check:
# n > 1 * 9 ? YES
# n = 12 - 9 = 3
# digit_len = 2
# count = 90
# start = 10
#
# Now:
# n = 3 lies in 2-digit numbers
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 2: FIND THE EXACT NUMBER
#
# Each number contributes `digit_len` digits.
#
# number index = (n - 1) // digit_len
#
# number = start + number index
#
# For n = 3:
# number = 10 + (3 - 1) // 2
# number = 10 + 1 = 11
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 3: FIND THE EXACT DIGIT
#
# digit_index = (n - 1) % digit_len
#
# digit_index = (3 - 1) % 2 = 0
#
# digit = first digit of "11" → '1'
# ---------------------------------------------------------

# ---------------------------------------------------------
# FINAL ANSWER:
# 1
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
